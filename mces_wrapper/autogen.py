# automatically generate Cpython wrapper file according to header files
# Run this script under mzd/serdes/mces_wrapper
# NOTE: this parser only support 1st order pointer; for higher level pointer please use another tool.

import glob
import os
import re
import logging
import shutil
from ctypes import *
import importlib
import time
import traceback


def rm_c_comments(lines):
    """
    remove C comments in the file to parse
    """
    m = re.compile(r'//.*')
    lines = re.sub(m, '', lines)
    m = re.compile(r'/\*.*?\*/', re.S)
    lines = re.sub(m, '', lines)

    return lines


class StructParse:
    """
    Parse the header files in the folder. Catch the enum types and sort them into enum_class.py
    """
    def __init__(self, h_file, enum_parser):
        self.h_files = h_file
        self.dll_name = 'MZDAPILib'                     # Name of CDLL
        self.dll_path = os.path.join('..', 'Debug', 'MZD.dll')
        self.struct_class_list = list()
        self.struct_pointer_dict = dict()               # key = name of struct pointer, value = name of struct
        self.macro_dict = dict()                        # key = name of macro, value = value of macro

        self.generate_macro_dict(enum_parser)
        self.generate_struct_class_list()

    class _Struct:
        """
        A class recording the name, member and type of a class
        """

        def __init__(self):
            self.struct_name = None
            self.struct_members = list()
            self.struct_types = list()
            self.pointer_flags = list()
            self.member_idc = list()

    def generate_macro_dict(self, enum_parser):
        for h_file in self.h_files:
            with open(h_file, 'r') as fp:
                contents = fp.read()
                contents = rm_c_comments(contents)
                m = re.compile(r'#define\s(\w+)\s+(\d+)')
                contents = re.findall(m, contents)                               # hexadecimal numbers not included
                for content in contents:
                    self.macro_dict[content[0]] = content[1]

        for enum in enum_parser.enum_class_list:
            for member, value in zip(enum.enum_members, enum.enum_values):
                self.macro_dict[member] = str(value)

    def generate_struct_class_list(self):
        # TODO: Read the manually written structure class for device, for such structures are complicated in C code...
        # with open('device_class.py') as fp:
        #     contents = fp.read()
        #     contents = re.findall(r'class\s+(\w+)[(]Structure[)]:\s+_fields_\s+=\s+\[([^\]]+)\]', contents)
        #     for content in contents:
        #         struct = self._Struct()
        #         struct.struct_name = content[0]
        #
        #         self.struct_class_list.append(struct)

        # parse header files
        for h_file in self.h_files:
            with open(h_file, 'r') as fp:
                contents = fp.read()
                contents = rm_c_comments(contents)
                contents = re.findall(r'typedef struct ([\s\w]+)[{]([^{}]+)[}]([\s\w,*]+);\s', contents)  # find all structure types
                for content in contents:
                    struct = self._Struct()
                    struct_name = re.sub(r'[\s]', '', content[2])
                    struct.struct_name = struct_name
                    # match: typedef struct _a{}a, *ap;
                    if re.search(r',\s*\*', struct_name):
                        struct.struct_name, struct_pointer_name = re.search(r'(\w+),\s*\*(\w+)', struct_name).groups()
                        self.struct_pointer_dict[struct_pointer_name] = struct.struct_name
                    struct_infos = content[1].split(';')
                    for struct_info in struct_infos:
                        struct_info = struct_info.strip()
                        # tmp = re.findall(r'([\[\]*\w\s]+)\s+([\[\]()*\w+-//]+)', struct_info)            # parse the members of structure
                        tmp = re.findall(r'([\[\]*\w\s]+)\s+([^;}]+)', struct_info)                        # parse the members of structure
                        if tmp:
                            member_type = tmp[0][0]
                            member_name = tmp[0][1]
                            member_type = member_type.strip()
                            member_name = member_name.strip()
                            # find the pointer, this part only support 1st order pointer
                            if member_type.endswith('*'):
                                struct.struct_types.append(member_type[:-1])
                                struct.struct_members.append(member_name)
                                struct.pointer_flags.append(True)
                            elif member_name.endswith('[]'):
                                struct.struct_types.append(member_type)
                                struct.struct_members.append(member_name[:-2])
                                struct.pointer_flags.append(True)
                            elif member_name.startswith('*'):
                                struct.struct_types.append(member_type)
                                struct.struct_members.append(member_name[1:])
                                struct.pointer_flags.append(True)
                            else:
                                struct.struct_types.append(member_type)
                                struct.struct_members.append(member_name)
                                struct.pointer_flags.append(False)

                    self.struct_class_list.append(struct)

    def convert_structure_class_to_ctype(self, type_dict):
        """
        Convert customized type to ctypes here; convert C array to legal python ctypes here.

        Since the member type of some structure is another class member, the order of definition of class has to be arranged so that structure_class.py
        can be imported as a python module.
        Therefore, I create an algorithm to set an index indicating the order in struct_class_list.

        Algorithm: Let B should be defined after A and C, the original order is ABC. To begin with, I set the order index as 1,2,3. Then, when I check B, I set
        the order index B as index(A) + index(C) + index(B). Then, index(B) will always be larger than A and C. Finally, by sorting order index with structure_class,
        I can get the correct order.
        """
        # make sure type dict and structure class are synchronized
        type_dict.structure_class_list = list()
        for struct in self.struct_class_list:
            type_dict.structure_class_list.append(struct.struct_name)

        order_idx = [f'{i}' for i in range(len(self.struct_class_list))]
        updated_struct_list = list()

        # convert struct_type to ctype
        for i, struct in enumerate(self.struct_class_list):
            updated_struct_members = list()
            updated_struct_types = list()
            for member, struct_type, pointer_flag in zip(struct.struct_members, struct.struct_types, struct.pointer_flags):
                idx = 0
                # check if member is array
                if '][' in member:    # high order array
                    expressions = re.findall(r'\[([\w\s*/+\-()]+)?\]', member)
                    idx = 1
                    member = re.search(r'(\w+)\[.*\]', member).group(1)
                    for expr in expressions:
                        items = re.findall(r'\w+', expr)
                        for item in items:
                            if self.macro_dict.get(item, 0):
                                # may have bug here.. Do not consider the condition that macro_1 is part of macro_2
                                expr = re.sub(item, self.macro_dict[item], expr)
                        try:
                            idx = idx * int(eval(expr))
                        except Exception:
                            traceback.print_exc()
                            logging.error(f'Unrecognized macro: {expr}.. {struct.struct_name}')

                elif '[' in member:  # 1 order array
                    if re.search(r'\w+\[([\s*/\-+\d()]+)\]', member):  # support +-/*
                        member, idx = re.search(r'(\w+)\[([\s*/\-+\d()]+)\]', member).groups()
                    elif re.search(r'\w+\[([\s*/\-+\d\w]+)\]', member):  # There is a macro within array index
                        member, idx = re.search(r'(\w+)\[([\s*/\-+\d()\w]+)\]', member).groups()
                        items = re.findall(r'\w+', idx)
                        for item in items:
                            if self.macro_dict.get(item, 0):
                                # may have bug here.. Do not consider the condition that macro_1 is part of macro_2
                                idx = re.sub(item, self.macro_dict[item], idx)
                    try:
                        idx = int(eval(idx))
                    except Exception:
                        traceback.print_exc()
                        logging.error(f'Unrecognized macro: {idx}... {struct.struct_name}')

                # convert struct_type to ctype
                if type_dict.basic_type_dict.get(struct_type, 0) or type_dict.special_type_dict.get(struct_type, 0):
                    struct_type = type_dict.basic_type_dict[struct_type]
                elif struct_type in type_dict.structure_class_list:
                    tmp = type_dict.structure_class_list.index(struct_type)
                    order_idx[i] += f' + eval(order_idx[{tmp}])'
                elif struct_type in type_dict.enum_class_list:
                    struct_type = 'c_int'
                else:
                    logging.warning(f'Unrecognized type!! struct_name = {struct.struct_name}, struct_type = {struct_type}')

                struct.member_idc.append(idx)
                updated_struct_members.append(member)
                updated_struct_types.append(struct_type)
            struct.struct_types = updated_struct_types
            struct.struct_members = updated_struct_members
            updated_struct_list.append(struct)

        # Sort the structure class
        order_idc = list()
        for idx in order_idx:
            idx = eval(idx)
            order_idc.append(idx)
        tmp = list(zip(order_idc, updated_struct_list))
        result = sorted(tmp, key=lambda x:x[0])
        self.struct_class_list = [item[1] for item in result]

    def write_structure_class_into_py(self):
        """
        generate struct_class.py. Since device structure is complicated... I just write the device structure by myself
        """
        with open('structure_class.py', 'w') as fp:
            fp.write('from ctypes import *\n\n')
            fp.write(f'\n{self.dll_name} = CDLL("{self.dll_path}")\n\n')
            for struct in self.struct_class_list:
                fp.write(f'class {struct.struct_name}(Structure):\n    _fields_ = [')
                info_list = []
                for member, struct_type, pointer_flag, idx in zip(struct.struct_members, struct.struct_types, struct.pointer_flags, struct.member_idc):
                    # check void
                    if pointer_flag:
                        struct_type = f'POINTER({struct_type})'
                    if idx:
                        info = '("' + f'{member}' + '", ' + f'{struct_type} * {idx}' + ')'
                    else:
                        info = '("' + f'{member}' + '", ' + f'{struct_type}' + ')'
                    info_list.append(info)
                info_list = ',\n                '.join(info_list)
                fp.write(f'{info_list}]\n\n\n')


class EnumParser:
    """
    Parse the header files in the folder. Catch the enum types and sort them into enum_class.py
    """
    def __init__(self, h_file):
        self.h_files = h_file
        self.enum_class_list = list()

        self.generate_enum_class_list()
        self.write_enum_class_into_py()

    class _Enum:
        """
        A class recording the name, members, values of a enumerate type
        """

        def __init__(self):
            self.enum_name = None
            self.enum_members = list()
            self.enum_values = list()

    def generate_enum_class_list(self):
        """
        generate enum_class.py
        """
        for h_file in self.h_files:
            with open(h_file) as fp:
                contents = fp.read()
                contents = rm_c_comments(contents)
                contents = re.findall(r'typedef enum[^;]+;', contents)  # find all enumerate types
                for content in contents:
                    enum = self._Enum()
                    tmp = re.split(r'[{}]', content)  # split the typedef enum{ *** } name;
                    enum_infos = re.sub(r'\s', '', tmp[1])
                    enum.enum_name = re.sub(r'[\s;]', '', tmp[2])
                    enum_infos = enum_infos.split(',')
                    enum_infos = list(filter(None, enum_infos))
                    for default_value, enum_info in enumerate(enum_infos):
                        if '=' in enum_info:
                            enum_member = enum_info.split('=')[0]
                            enum_value = enum_info.split('=')[1]
                            if '0x' in enum_value:
                                enum_value = int(enum_value, 16)
                        else:
                            enum_member = enum_info
                            enum_value = default_value

                        enum.enum_members.append(enum_member)
                        enum.enum_values.append(enum_value)

                    self.enum_class_list.append(enum)

    def write_enum_class_into_py(self):
        with open('enum_class.py', 'w') as f:
            f.write('from enum import Enum, unique\n\n')
            for enum in self.enum_class_list:
                f.write(f'@unique\nclass {enum.enum_name}(Enum):\n')
                for member, value in zip(enum.enum_members, enum.enum_values):
                    f.write(f'    {member} = {value}\n')
                f.write('\n\n')


class TypeDict:
    """
    Parse the header files in the folder. Get the mapping relationship between customized types and C types
    """
    def __init__(self, enum_parser, struct_parser):
        self.basic_type_dict = dict()
        self.special_type_dict = dict()
        self.enum_class_list = list()
        self.structure_class_list = list()
        self.structure_pointer_dict = struct_parser.struct_pointer_dict
        self.func_pointer_dict = dict()                                 # key = name of function pointer, value = its ctype
        self.macro_dict = dict()                                        # key = name of macro, value = value of macro

        self.load_basic_type_dict()
        self.load_special_type_dict()
        # self.load_device_class()
        self.load_func_pointer_dict()

        # load structure/enumerate class list
        for struct in struct_parser.struct_class_list:
            self.structure_class_list.append(struct.struct_name)
        for enum in enum_parser.enum_class_list:
            self.enum_class_list.append(enum.enum_name)

    def load_basic_type_dict(self):
        # Common basic types in C
        key_list = ['int8_t', 'int16_t', 'int32_t', 'int64_t', 'uint8_t', 'uint16_t', 'uint32_t', 'uint64_t', 'unsigned int', 'int', 'float', 'double', 'char', 'const char', 'unsigned char']
        value_list = ['c_int8', 'c_int16', 'c_int32', 'c_int64', 'c_uint8', 'c_uint16', 'c_uint32', 'c_uint64', 'c_uint', 'c_int', 'c_float', 'c_double', 'c_char', 'c_char', 'c_ubyte']
        for key, value in zip(key_list, value_list):
            self.basic_type_dict[key] = value

        #  customized basic types in MCESD
        key_list = ['MCESD_8', 'MCESD_16', 'MCESD_32', 'MCESD_64', 'MCESD_U8', 'MCESD_U16', 'MCESD_U32', 'MCESD_U64', 'MCESD_S8', 'MCESD_S16', 'MCESD_STATUS', 'MCESD_UINT', 'MCESD_INT']
        value_list = ['c_int8', 'c_int16', 'c_int32', 'c_int64', 'c_uint8', 'c_uint16', 'c_uint32', 'c_uint64', 'c_int8', 'c_int16', 'c_uint32', 'c_uint', 'c_int']
        for key, value in zip(key_list, value_list):
            self.basic_type_dict[key] = value

        #  customized basic types in MZD
        key_list = ['MZD_8', 'MZD_16', 'MZD_32', 'MZD_64', 'MZD_U8', 'MZD_U16', 'MZD_U32', 'MZD_U64', 'MZD_S8', 'MZD_S16', 'MZD_STATUS', 'MZD_UINT', 'MZD_INT', 'MZD_VOID']
        value_list = ['c_int8', 'c_int16', 'c_int32', 'c_int64', 'c_uint8', 'c_uint16', 'c_uint32', 'c_uint64', 'c_int8', 'c_int16', 'c_uint32', 'c_uint', 'c_int', 'c_int']
        for key, value in zip(key_list, value_list):
            self.basic_type_dict[key] = value

    def load_special_type_dict(self):
        key_list = ['MCESD_DEV_PTR', 'MZD_PVOID', 'MZD_DEV_PTR', 'Device_Handle_t']
        value_list = ['c_void_p', 'c_void_p', 'c_void_p', 'c_void_p']
        for key, value in zip(key_list, value_list):
            self.special_type_dict[key] = value

    def load_device_class(self):
        with open('device_class.py') as fp:
            content = fp.read()
            self.structure_class_list = re.findall(r'class ([\w]+)[(]Structure[)]', content)

    def load_func_pointer_dict(self):
        # manually write function pointer here
        self.func_pointer_dict['MZD_FUNC_WAIT'] = 'CFUNCTYPE(c_void_p, c_uint)'
        self.func_pointer_dict['FMCESD_READ_REG'] = 'CFUNCTYPE(c_void_p, c_uint32, POINTER(c_uint32))'
        self.func_pointer_dict['FMCESD_WRITE_REG'] = 'CFUNCTYPE(c_void_p, c_uint32, c_uint32)'
        self.func_pointer_dict['MZD_FUNC_WRITE_MDIO'] = 'CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, c_uint16)'
        self.func_pointer_dict['MZD_FUNC_READ_MDIO'] = 'CFUNCTYPE(c_void_p, c_uint16, c_uint16, c_uint16, POINTER(c_uint16))'


class FunctionParser:
    """
    Automatically parse the header files
    """
    def __init__(self, h_file, type_dict):
        self.h_files = h_file
        self.type_dict = type_dict
        self.func_list = list()
        self.wrapper = 'mzdFunctionLib.py'             # Name of Output wrapper
        self.dll_name = 'MZDAPILib'                     # Name of CDLL
        self.dll_path = os.path.join('..', 'Debug', 'MZD.dll')
        self.testcase = 'Testcases_all.py'              # Output testcase

        self.parse()
        # self.write_funcs_to_wrapper()

    class _Func:
        """
        A class recording the function name, type of return value and arguments
        """

        def __init__(self):
            self.func_name = None
            self.ret_type = None
            self.header_file = None
            self.parameters = list()

        def get_arg_names(self):
            ret = list()
            for param in self.parameters:
                if param.arg_pointer_flag:
                    ret.append(param.arg_name + '_p')
                else:
                    ret.append(param.arg_name)
            return ', '.join(ret)

    class _Param:
        """
        A class recording the information of the parameter of a C function
        """
        def __init__(self, param_info=(None, None, None)):
            self.arg_pointer_flag = False
            arg_info = list()
            for info in param_info:
                if info and ('*' in info or '[' in info):
                    self.arg_pointer_flag = True
                    info = re.sub(r'[\[\]*]', '', info)
                arg_info.append(info)

            self.arg_inout = arg_info[0]  # IN/ OUT
            self.arg_type = arg_info[1].strip()
            self.arg_name = arg_info[2]

    def parse(self):
        """
        parse all the header files in the target folder;
        get all the functions to be wrapped.
        save those function information(name, argument type, return type) in func_list
        """
        for h_file in self.h_files:
            with open(h_file) as fp:
                contents = fp.read()

                contents = rm_c_comments(contents)
                # contents = re.findall(r'MCESD_FUNC ([*\w]+) ([\w]+)([^;]+)', contents)  # find all functions
                contents = re.findall(r'MZD_FUNC ([*\w]+) ([\w]+)([^;]+)', contents)  # find all functions
                # For each function
                for content in contents:
                    func = self._Func()
                    ret_type = content[0]
                    if self.type_dict.basic_type_dict.get(ret_type, 0):
                        func.ret_type = self.type_dict.basic_type_dict[ret_type]
                    else:
                        logging.error(f'Unrecognized ret type {ret_type}')
                    func.func_name = content[1]
                    param_infos = re.sub(r'[\n()]', '', content[2])                          # remove () and \n in parameters
                    param_infos = param_infos.split(',')
                    for param_info in param_infos:
                        param_info = re.search(r'(IN|OUT)\s+([\[\]*\w\s]+)\s+([\[\]*\w]+)', param_info).groups()
                        param = self._Param(param_info=param_info)

                        # convert customized variable type to ctype according to the type dict
                        arg_type = param.arg_type
                        if self.type_dict.special_type_dict.get(arg_type, 0):           # special type dict should be at the very beginning
                            arg_type = self.type_dict.special_type_dict[arg_type]
                        elif self.type_dict.basic_type_dict.get(arg_type, 0):
                            arg_type = self.type_dict.basic_type_dict[arg_type]
                        elif arg_type in self.type_dict.enum_class_list:
                            pass
                        elif arg_type in self.type_dict.structure_class_list:
                            pass
                        elif self.type_dict.structure_pointer_dict.get(arg_type, 0):
                            arg_type = self.type_dict.structure_pointer_dict[arg_type]
                            param.arg_pointer_flag = True
                        elif self.type_dict.func_pointer_dict.get(arg_type, 0):
                            arg_type = self.type_dict.func_pointer_dict[arg_type]
                            param.arg_pointer_flag = True
                        else:
                            logging.warning(f'No valid type: {arg_type}； func_name: {func.func_name}')
                        param.arg_type = arg_type
                        func.parameters.append(param)

                    func.header_file = os.path.basename(h_file)

                    self.func_list.append(func)

    def write_funcs_to_wrapper(self):
        # initialize the wrapper
        shutil.copyfile('structure_class.py', self.wrapper)

        for func in self.func_list:
            with open(self.wrapper, 'a') as fp:
                arg_names = func.get_arg_names()
                fp.write(f'def {func.func_name}({arg_names}):\n')

                # Comment of this function
                fp.write('    """\n')
                arg_types = list()
                for param in func.parameters:
                    arg_type = param.arg_type
                    arg_name = param.arg_name
                    if arg_type in self.type_dict.enum_class_list:
                        if param.arg_pointer_flag:
                            arg_types.append('POINTER(c_int)')
                            fp.write(f'    :param {arg_name}_p: A pointer of the enumerate class {arg_type}\n')
                        else:
                            arg_types.append('c_int')
                            fp.write(f'    :param {arg_name}: member from enumerate class {arg_type}\n')
                    elif arg_type in self.type_dict.structure_class_list:
                        if param.arg_pointer_flag:
                            arg_types.append(f'POINTER({arg_type})')
                            fp.write(f'    :param {arg_name}_p: A pointer of the structure class {arg_type}\n')
                        else:
                            arg_types.append(arg_type)
                            fp.write(f'    :param {arg_name}: implementation of the structure class {arg_type}\n')
                    else:
                        if param.arg_pointer_flag and arg_type != 'c_void_p':
                            arg_types.append(f'POINTER({arg_type})')
                            fp.write(f'    :param {arg_name}_p: A pointer of {arg_type}\n')
                        else:
                            arg_types.append(arg_type)
                            fp.write(f'    :param {arg_name}: argument type {arg_type}\n')
                fp.write('    """\n')

                fp.write(f'    func = {self.dll_name}["{func.func_name}"]\n')
                arg_types = ', '.join(arg_types)
                fp.write(f'    func.argtypes = [{arg_types}]\n')
                fp.write(f'    func.restype = {func.ret_type}\n')
                fp.write(f'    ret = func({arg_names})\n')
                fp.write(f'    return ret\n\n\n')

    def write_testcase(self):
        """
        Automatically generate testcases
        """
        shutil.copyfile('testcase_template.py', self.testcase)

        basic_type_list = ['c_int8', 'c_int16', 'c_int32', 'c_int64', 'c_uint8', 'c_uint16', 'c_uint32', 'c_uint64', 'c_uint', 'c_int', 'c_float', 'c_double', 'c_char', 'c_char']
        with open(self.testcase, 'a') as fp:
            for func in self.func_list:
                arg_names = list()
                logging_infos = list()
                init_param_infos = list()
                for param in func.parameters:
                    arg_type = param.arg_type
                    arg_name = param.arg_name
                    # common param
                    if arg_type == 'c_void_p':
                        pass
                    elif arg_type in basic_type_list:
                        init_param_infos.append(f'    {arg_name} = 1\n')  # maybe we could iterate/ lane ranges from 0, 1, 2, 3
                        if param.arg_pointer_flag:
                            init_param_infos.append(f'    {arg_name}_p = {arg_type}({arg_name})\n')
                            logging_infos.append(f'    logging.debug(f"{arg_name}' + ' = {' + f'{arg_name}_p.value' + '}")\n')
                            arg_name = arg_name + '_p'
                        else:
                            logging_infos.append(f'    logging.debug(f"{arg_name}' + ' = {' + f'{arg_name}' + '}")\n')
                    elif arg_type in self.type_dict.enum_class_list:
                        member_names = eval(arg_type).__dict__['_member_names_']
                        init_param_infos.append(f'    {arg_name} = {arg_type}.{member_names[0]}.value\n')  # maybe we could iterate
                        if param.arg_pointer_flag:
                            init_param_infos.append(f'    {arg_name}_p = {arg_type}({arg_name})\n')
                            logging_infos.append(f'    logging.debug(f"{arg_name}' + ' = {' + f'{arg_name}_p.value' + '}")\n')
                            arg_name = arg_name + '_p'
                        else:
                            logging_infos.append(f'    logging.debug(f"{arg_name}' + ' = {' + f'{arg_name}' + '}")\n')
                    elif arg_type in self.type_dict.structure_class_list:
                        attr_inits = []
                        attr_list = eval(arg_type).__dict__['_fields_']
                        for attr in attr_list:
                            print(attr)
                            attr_name = attr[0]
                            attr_class = attr[1]
                            # TODO: if the parameter of structure class is an array
                            # if '*' in attr_class:
                            #     idx = attr_class.split('*')[1]

                            if attr_class == c_bool:
                                attr_inits.append('0')  # 0 or 1
                            else:
                                attr_inits.append('0')  # Just give it an initial value... Usually it is used for OUT
                        attr_init = ', '.join(attr_inits)
                        init_param_infos.append(f'    {arg_name} = {arg_type}({attr_init})\n')
                        logging_infos.append(f'    logging.debug(f"{arg_name}' + ' = {' + f'{arg_type}.{attr_name}' + '}")\n')
                        if param.arg_pointer_flag:
                            init_param_infos.append(f'    {arg_name}_p = byref({arg_name})\n')
                            arg_name = arg_name + '_p'
                    elif 'CFUNCTYPE' in arg_type:
                        # function pointer, which means this is a device initiation function. I should manually write it
                        logging_infos = list()
                        break
                    else:
                        logging.warning(f'Unrecognized arg_type {arg_type}; func_name {func.func_name}; arg_name {arg_name}')
                    arg_names.append(arg_name)

                if logging_infos:
                    params = ', '.join(arg_names)
                    fp.write(f'    logging.info("Function name : {func.func_name}")\n')
                    for init_param_info in init_param_infos:
                        fp.write(f'{init_param_info}')
                    fp.write(f'    try:\n        {func.func_name}({params})\n    except Exception:\n        traceback.print_exc()\n')

                    for logging_info in logging_infos:
                        fp.write(f'{logging_info}')
                    fp.write('    logging.info("\\n")\n')
                    fp.write('\n')


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s! File: %(filename)s Line %(lineno)d; Msg: %(message)s', datefmt='%d-%M-%Y %H:%M:%S')

    h_files = list()
    file_path_list = ['..\mzd\*.h', '..\mzd\serdes\*.h', '..\mzd\serdes\C112GX4\*.h', '..\mzd\ptp\*.h', '..\mzd\macsec\*.h']
    for file_path in file_path_list:
        h_files.extend(glob.glob(file_path))
    enum_parser = EnumParser(h_files)
    struct_parser = StructParse(h_files, enum_parser)
    type_dict = TypeDict(enum_parser, struct_parser)
    struct_parser.convert_structure_class_to_ctype(type_dict)
    # struct_parser.write_structure_class_into_py()

    h_files = list()
    file_path_list = ['..\mzd\*.h']
    for file_path in file_path_list:
        h_files.extend(glob.glob(file_path))
    head_parser = FunctionParser(h_files, type_dict)
    # TODO: add reload// use a more pleasant way
    from enum_class import *
    from structure_class import *
    head_parser.write_testcase()

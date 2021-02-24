# automatically generate Cpython wrapper file according to header files
# Run this script under mzd/serdes/mces_wrapper

import glob
import os
import re
import logging
import shutil
from ctypes import *
from structure_class import *
import time


class Func:
    """
    A class recording the function name, type of return value and arguments
    """
    def __init__(self):
        self.func_name = None
        self.arg_types = list()
        self.arg_names = list()
        self.arg_pointer_flags = list()
        self.ret_types = None
        self.header_file = None
        self.arg_inout_list = list()


class _Enum:
    """
    A class recording the name, members, values of a enumerate type
    """
    def __init__(self):
        self.enum_name = None
        self.enum_members = list()
        self.enum_values = list()


class TypeParser:
    """
    Parse the header files in the folder. Get the mapping relationship between customized types and C types
    """
    def __init__(self):
        self.folder = os.path.join('..', 'C112GX4')
        self.basic_type_dict = dict()
        self.enum_class_list = list()
        self.structure_class_list = list()
        self.special_type_dict = dict()

        self.generate_enum_class()
        # load
        # self.load_basic_type_dict()
        # self.load_enum_class_list()
        # self.load_structure_class_list()
        # self.load_special_type_dict()

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

    def load_special_type_dict(self):
        key_list = ['MCESD_DEV_PTR', 'MCESD_FIELD_PTR']
        value_list = ['c_void_p', 'POINTER(MCESD_FIELD)']
        for key, value in zip(key_list, value_list):
            self.special_type_dict[key] = value

    def load_enum_class_list(self):
        with open('enum_class.py') as fp:
            lines = fp.readlines()

        for line in lines:
            if re.match(r'class .*\(Enum\):', line):
                self.enum_class_list.append(line[6:-8])

    def load_structure_class_list(self):
        with open('structure_class.py') as fp:
            lines = fp.readlines()

        for line in lines:
            if re.match(r'class .*\(Structure\):', line):
                self.structure_class_list.append(line[6:-13])

    def generate_enum_class(self):
        """
        generate enum_class.py
        """
        with open('enum_class.py', 'w') as fp:
            fp.write('from enum import Enum, unique\n\n')
        h_files = glob.glob(os.path.join(self.folder, '*.h'))
        h_files.append(os.path.join('..', 'mcesdApiTypes.h'))

        for h_file in h_files:
            with open(h_file) as fp:
                contents = fp.read()
                contents = contents.split('typedef enum')
                contents.pop(0)
                for content in contents:
                    enum = _Enum()
                    enum_info = content.split(';')[0].replace('\n', '')
                    enum_info = enum_info.split('}')
                    enum.enum_name = enum_info[1].strip()
                    enum_info = enum_info[0].split('{')[1]
                    enum_infos = enum_info.split(',')
                    enum_infos = list(filter(None, enum_infos))
                    for default_value, enum_info in enumerate(enum_infos):
                        if '=' in enum_info:
                            enum_member = enum_info.split('=')[0].strip()
                            # remove the comments
                            if '/*' in enum_member:
                                enum_member = enum_member.split('*/')[1].strip()
                            enum_value = enum_info.split('=')[1].strip()
                            if '/*' in enum_value:
                                enum_value = enum_value.split('/*')[0].strip()
                            if '0x' in enum_value:
                                enum_value = int(enum_value.strip(), 16)
                        elif '/*' in enum_info:
                            enum_member = enum_info.split('*/')[1].strip()
                            if enum_member == '':
                                continue
                            else:
                                enum_value = default_value
                        else:
                            enum_value = default_value
                            enum_member = enum_info
                        enum.enum_values.append(enum_value)
                        enum.enum_members.append(enum_member)

                    with open('enum_class.py', 'a') as fp:
                        fp.write(f'@unique\nclass {enum.enum_name}(Enum):\n')
                        for member, value in zip(enum.enum_members, enum.enum_values):
                            fp.write(f'    {member} = {value}\n')
                        fp.write('\n\n')


class HeaderParser:
    """
    Automatically parse the header files
    """
    def __init__(self):
        self.folder = os.path.join('..', 'C112GX4')
        self.type_parser = TypeParser()
        self.func_list = list()
        self.wrapper = 'mcesFunctionLib.py'
        self.dll_name = 'MZDAPILib'
        self.testcase = 'Testcases_all.py'

    def parse(self):
        """
        parse all the header files in the target folder;
        get all the functions to be wrapped.
        save those function information(name, argument type, return type) in func_list
        """
        for h_file in glob.glob(os.path.join(self.folder, '*.h')):
            with open(h_file) as fp:
                contents = fp.read()
                contents = contents.split('MCESD_STATUS ')
                contents.pop(0)
                for content in contents:
                    func = Func()
                    func_info = content.split(');')[0]
                    func_name = func_info.split('(')[0].replace('\n', '')
                    func_args = func_info.split('(')[1].replace('\n', '')
                    func_args = func_args.split(',')

                    func.func_name = func_name
                    func_arg_stripped = [func_arg.strip() for func_arg in func_args]
                    for func_arg in func_arg_stripped:
                        params = func_arg.split()
                        arg_name = params.pop()
                        if '*' in arg_name:
                            arg_name = arg_name[1:]
                            func.arg_pointer_flags.append(1)
                        elif '[]' in arg_name:
                            arg_name = arg_name[:-2]
                            func.arg_pointer_flags.append(1)
                        elif '[ ]' in arg_name:
                            arg_name = arg_name[:-3]
                            func.arg_pointer_flags.append(1)
                        else:
                            func.arg_pointer_flags.append(0)

                        arg_inout = params.pop(0)

                        if len(params) > 1:
                            arg_type = ' '.join(params)
                        else:
                            arg_type = params[0]

                        if self.type_parser.basic_type_dict.get(arg_type, 0):
                            arg_type = self.type_parser.basic_type_dict[arg_type]
                        elif arg_type in self.type_parser.enum_class_list:
                            pass
                        elif arg_type in self.type_parser.structure_class_list:
                            pass
                        elif self.type_parser.special_type_dict.get(arg_type, 0):
                            if arg_type == 'MCESD_FIELD_PTR':
                                arg_type = 'MCESD_FIELD'
                                func.arg_pointer_flags.append(1)
                            else:
                                arg_type = self.type_parser.special_type_dict[arg_type]
                        else:
                            logging.warning(f'No valid type: {arg_type}； func_name: {func_name}')

                        func.arg_inout_list.append(arg_inout)
                        func.arg_types.append(arg_type)
                        func.arg_names.append(arg_name)
                        func.ret_types = 'c_uint32'
                        func.header_file = os.path.basename(h_file)

                    self.func_list.append(func)

    def write_funcs_to_wrapper(self):
        # initialize the wrapper
        shutil.copyfile('structure_class.py', self.wrapper)

        for func in self.func_list:
            with open(self.wrapper, 'a') as fp:
                arg_names = ', '.join(func.arg_names)
                fp.write(f'def {func.func_name}({arg_names}):\n')

                # Comment of this function
                fp.write('    """\n')
                arg_types = list()
                for arg_type, arg_name, flag in zip(func.arg_types, func.arg_names, func.arg_pointer_flags):
                    if arg_type in self.type_parser.enum_class_list:
                        if flag:
                            arg_types.append('POINTER(c_int)')
                            fp.write(f'    :param {arg_name}: A pointer of the enumerate class {arg_type}\n')
                        else:
                            arg_types.append('c_int')
                            fp.write(f'    :param {arg_name}: member from enumerate class {arg_type}\n')
                    elif arg_type in self.type_parser.structure_class_list:
                        if flag:
                            arg_types.append(f'POINTER({arg_type})')
                            fp.write(f'    :param {arg_name}: A pointer of the structure class {arg_type}\n')
                        else:
                            arg_types.append(arg_type)
                            fp.write(f'    :param {arg_name}: implementation of the structure class {arg_type}\n')
                    else:
                        if flag:
                            arg_types.append(f'POINTER({arg_type})')
                            fp.write(f'    :param {arg_name}: A pointer of {arg_type}\n')
                        else:
                            arg_types.append(arg_type)
                            fp.write(f'    :param {arg_name}: argument type {arg_type}\n')
                fp.write('    """\n')

                fp.write(f'    func = {self.dll_name}["{func.func_name}"]\n')
                arg_types = ', '.join(arg_types)
                fp.write(f'    func.argtypes = [{arg_types}]\n')
                fp.write(f'    func.restype = {func.ret_types}\n')
                fp.write(f'    ret = func({arg_names})\n')
                fp.write(f'    return ret\n\n\n')

    def write_testcase(self):
        """
        Automatically generate testcases
        """
        shutil.copyfile('testcase_template.py', self.testcase)

        basic_type_list = ['c_int8', 'c_int16', 'c_int32', 'c_int64', 'c_uint8', 'c_uint16', 'c_uint32', 'c_uint64', 'c_uint', 'c_int', 'c_float', 'c_double', 'c_char', 'c_char']
        for func in self.func_list:
            with open(self.testcase, 'a') as fp:
                fp.write(f'    logging.info("Function name : {func.func_name}")\n')
                arg_names = list()
                logging_infos = list()
                for arg_type, arg_name, flag in zip(func.arg_types, func.arg_names, func.arg_pointer_flags):
                    # common param
                    if arg_type in basic_type_list:
                        fp.write(f'    {arg_name} = 1\n')       # maybe we could iterate/ lane ranges from 0, 1, 2, 3
                        logging_infos.append(f'    logging.debug(f"{arg_name}' + ' = {' + f'{arg_name}' + '}")\n')
                        if flag:
                            fp.write(f'    {arg_name}_p = {arg_type}({arg_name})\n')
                            arg_name = arg_name + '_p'
                    elif arg_type in self.type_parser.enum_class_list:
                        member_names = eval(arg_type).__dict__['_member_names_']
                        fp.write(f'    {arg_name} = {arg_type}.{member_names[0]}.value\n')    # maybe we could iterate
                        logging_infos.append(f'    logging.debug(f"{arg_name}' + ' = {' + f'{arg_name}' + '}")\n')
                        if flag:
                            fp.write(f'    {arg_name}_p = c_long({arg_name})\n')
                            arg_name = arg_name + '_p'
                    elif arg_type in self.type_parser.structure_class_list:
                        attr_inits = []
                        attr_list = eval(arg_type).__dict__['_fields_']
                        for attr in attr_list:
                            attr_name = attr[0]
                            attr_class = attr[1]
                            if attr_class == c_bool:
                                attr_inits.append('0')            # 0 or 1
                            else:
                                attr_inits.append('0')            # Just give it an initial value... Usually it is used for OUT
                        attr_init = ', '.join(attr_inits)
                        fp.write(f'    {arg_name} = {arg_type}({attr_init})\n')
                        logging_infos.append(f'    logging.debug(f"{arg_name}' + ' = {' + f'{arg_type}.{attr_name}' + '}")\n')
                        if flag:
                            fp.write(f'    {arg_name}_p = byref({arg_name})\n')
                            arg_name = arg_name + '_p'
                    elif arg_name == 'devPtr':
                        fp.write(f'    {arg_name} = apiWrapper.pSerdesDev\n')
                    else:
                        logging.warning(f'Unrecognized arg_type {arg_type}')
                    arg_names.append(arg_name)
                params = ', '.join(arg_names)
                fp.write(f'    try:\n        {func.func_name}({params})\n    except Exception:\n        traceback.print_exc()\n')

                for logging_info in logging_infos:
                    fp.write(f'{logging_info}')
                fp.write('    logging.info("\\n")\n')
                fp.write('\n')


if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s! File: %(filename)s Line %(lineno)d; Msg: %(message)s', datefmt='%d-%M-%Y %H:%M:%S')
    # cur_time = time.strftime("%m-%d-%Y_%H-%M-%S", time.localtime())
    # logging.basicConfig(level=logging.WARNING,
    #                     filename=f'X93160_API_test_{cur_time}.log',
    #                     format='%(levelname)s: %(message)s',
    #                     datefmt='%d-%M-%Y %H:%M:%S')

    head_parser = HeaderParser()
    # head_parser.parse()
    # head_parser.write_funcs_to_wrapper()
    # head_parser.write_testcase()






## Generate C to python wrapper automatically
This a simple tool, which mainly focus on generating ctypes python wrapper on embedded C project.
The major idea of this tool is to parse header files/C files and grasp the definition of functions 
and customized variable types, then rewrite them in Ctypes style.

### How to use
1. Edit config.json
2. Optional: edit device_class.py. Some C structures are complex which contains ifdef/endif...
   Please leave those structures in device_class.py. The format is in Ctypes standard.
3. Run autogen.py

### How to use Ctypes Wrapper
You need to compile the C project and generate a dynamic lib(.dll in windows and .so in Linux).
Cpython support loading dll files while running C and will call the C function according to its name.
This wrapper is an interface to wrap those C function into a python function.

### Limitation
1. Do not support #ifdef #endif...
2. Do not support nested parsing... e.g. the parameter of a function pointer is another function pointer
3. Only support three types of typedef: enum, struct and definition of struct+struct_pointer in one command.
4. Only support simplest macros like this: #define VAR_NAME 0


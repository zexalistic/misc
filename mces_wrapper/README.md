## Generate C to python wrapper automatically
This a simple tool, which mainly focus on generating ctypes python wrapper on embedded C project.
The major idea of this tool is to parse header files/C files and grasp the definition of functions 
and customized variable types, then rewrite them in Ctypes style.

### How to use
1. Edit config.json
2. Run autogen.py

### How to use Ctypes Wrapper
You need to compile the C project and generate a dynamic lib(.dll in windows and .so in Linux).
Cpython support loading dll files while running C and will call the C function according to its name.
This wrapper is an interface to wrap those C function into a python function.

### Limitation
1. Do not support #ifdef #endif...
2. Do not support nested citation. e.g. the parameter of a function pointer is another function pointer
3. Do not support union at present...
4. Only support simplest macros like this: #define VAR_NAME 0

### For more information
You can see the samples in this folder.


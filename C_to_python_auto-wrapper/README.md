## Generate C to python wrapper automatically
This tool mainly focus on generating ctypes python wrapper on embedded C project.

The major idea of this tool is to parse header/C files and grasp the definition of functions 
and customized variable types, then rewrite them in Ctypes style.

### How to use
1. Build dll files(Optional, if you want to run testcases)
2. Edit config.json
3. Run autogen.py

### Output
* wrapper.py : the python wrapper of C functions written in ctypes style
* Testcase_all.py: simple auto-generated testcases templates. You had better check it before running. 
* You can change the names of output files in config.json

### How to use Ctypes Wrapper
You need to compile the C project and generate a dynamic lib(.dll in windows).
Cpython support loading dll files while running C and will call the C function according to its name.
This wrapper is an interface to wrap those C function into a python function.

### Limitation
1. Do not support #ifdef #endif...
2. Do not support nested citation. e.g. the parameter of a function pointer is another function pointer
3. Do not support union at present...
4. Only support simplest macros like this: #define VAR_NAME 0
5. Parameter of function can not be void...
6. Only support typedef enum. not support direct definition of enum type.
7. Parenthesis may affect the parsing result, e.g. ((a)) may have a different parsing result with a

### For more information
You can see Samples/.
The default settings are based on the samples.

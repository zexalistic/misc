## Generate C to python wrapper automatically
This a simple tool, which mainly focus on generating Cpython wrapper on embedded C project.
The major idea of this tool is to parse header files and grasp the definition of functions 
and customized variable types, then rewrite them in Cpython style.

### How to use
Follow the comment in config.json and change the value of parameters into your own value

Run autogen.py

### Limitation
1. Do not support #ifdef #endif...
2. Do not support nested parsing... e.g. the parameter of a function pointer is another function pointer
3. Only support three types of typedef: enum, struct and definition of struct+struct_pointer in one command.
4. Only support simplest macros like this: #define VAR_NAME 0


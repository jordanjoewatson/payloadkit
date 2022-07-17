# README

````
┌─┐┌─┐┬ ┬┬  ┌─┐┌─┐┌┬┐┬┌─┬┌┬┐
├─┘├─┤└┬┘│  │ │├─┤ ││├┴┐│ │ 
┴  ┴ ┴ ┴ ┴─┘└─┘┴ ┴─┴┘┴ ┴┴ ┴
   v1.0 @jordanjoewatson
````

An offensive security framework for writing payloads

More coming soon... v1.0 is just a PoC

## Modules
- C++ XOR
- C++ ROT13
- C# XOR
- C# DLLImports (v1.0 acceptable functionality)
- C# AES
- PowerShell XOR
- Visual Basic XOR
- Cobalt Strike DLLImports (v1.0 acceptable functionality)

## Directory structure

- modules - directory containing all modules

Each module is listed in modules.language.modulename
Under each module directory the modulename.py file should contain a class of Modulename which has a class run(). the run function accepts the arguments of the module passed in from the command line, this will then run the function, and write a directory containing all of the files output for the module

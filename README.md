# README

````
  ┌─┐┌─┐┬ ┬┬  ┌─┐┌─┐┌┬┐┬┌─┬┌┬┐
  ├─┘├─┤└┬┘│  │ │├─┤ ││├┴┐│ │ 
  ┴  ┴ ┴ ┴ ┴─┘└─┘┴ ┴─┴┘┴ ┴┴ ┴
     v1.0 @jordanjoewatson
````

An offensive security framework for writing payloads.

Purpose of the framework is to take a binary, the tool then generates various mutations of the binary depending on the module. For example, the C# AES module will create base16, base64, hex and int versions, and provides C# functions to decrypt the encrypted binary. These generated segments of code can easily be added into a payload.

More modules soon.

## Modules
- C++ XOR
- C++ ROT13
- C# XOR
- C# DLLImports (limited imports available)
- C# AES
- PowerShell XOR
- Visual Basic XOR
- Cobalt Strike DLLImports (limited imports available)
- Format C Hex String
- Format Hex String
- Format Int Array
- Format Hex Array

## Setup

````
python3 -m venv ./venv
source venv/bin/activate
pip3 install -r requirements
python3 payloadkit.py
````
## Usage: payloadkit CLI

payloadkit uses the python `typer` module. The tool has three options
- `ls`
- `ìnfo`
- `run`

### `ls`

````
python3 payloadkit.py ls
````

Lists all modules available

### `info`

````
python3 payloadkit.py info <modulename>
````

Prints out information on module, such as arguments required and description of module

### `run`

````
python3 payloadkit.py run <modulename> [YAML/Args]
````

## Usage: Modules

Some modules require a string argument, some modules require a YAML file

### C++ XOR

Config
````
key: this is my key
payload: ./path/to/payload.bin
````

Run
````
python3 payloadkit.py run cpp.xor xor.yaml
````

### C++ ROT13

Config
````
payload: /path/to/payload.bin
````

Run
````
`python3 payloadkit.py run cpp.rot13 rot13.yaml
````

### C# AES

Config
````
blocksize: AES-256
payload: /path/to/payload.bin
````

Run
````
python3 payloadkit.py run csharp.aes aes.yaml
````

### C# DllImports

Fetches DllImport statements to use in payloads, doesn't require a YAML file. Only a few imports are currently available but planning to add more with time

Run
````
python3 payloadkit.py run cobaltstrike.dllimport malloc
````

### C# XOR

Config
````
key: this is my XOR key
payload: /path/to/payload.bin
````

Run
````
python3 payloadkit.py run csharp.xor xor.yaml
````

### PowerShell XOR

Config
````
key: this is my XOR key
payload: /path/to/payload.bin
````

Run
````
python3 payloadkit.py run powershell.xor xor.yaml
````

### Cobalt Strike DllImports

Fetches DllImport statements to use in payloads, doesn't require a YAML file. Only a few imports are currently available but planning to add more with timeS

Run
````
python3 payloadkit.py run cobaltstrike.dllimport malloc
````

### Visual Basic XOR

Config 
````
key: this is my XOR key
payload: /path/to/payload.bin
````

Run 
````
python3 payloadkit.py run visualbasic.xor xor.yaml
````

### Format C Hex String

Uses a single argument for a filepath, reads in as bytes and writes out in the format of a C Hex string, e.g. "\\xAB\\xCD..."

Run
````
python3 payloadkit.py run format.chexstring /path/to/binary.bin
````

### Format Hex String

Uses a single argument for a filepath, reads in as bytes and writes out in the format of a Hex string, e.g. "ABCD..."

````
python3 payloadkit.py run format.hexstring /path/to/binary.bin
````

### Format Int Array

Uses a single argument for a filepath, reads in as bytes and writes out in the format of a C Hex string, e.g. 41,42,...

Run
````
python3 payloadkit.py run format.intarray /path/to/binary.bin
````

### Format Hex Array

Uses a single argument for a filepath, reads in as bytes and writes out in the format of a hex array, e.g. \\xAB,\\xCD,...

Run
````
python3 payloadkit.py run format.hexarray /path/to/binary.bin
````

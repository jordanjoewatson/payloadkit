from modules.Module import Module
from jinja2 import Template 
import os
from base64 import b64encode
from misc.utils import lines, create_hex_string, create_int_string

"""
Need to add options somehow
"""
class rot13(Module):

    options = {
        'payload': { 'desc': 'path to a payload to encrypt', 'required': True },
        'output': { 'desc': 'directory to write files to, otherwise writes to, otherwise writes files to ./output/', 'required': False }
    }

    input_type = "yaml"
    module_type = "payload" # change this to something else

    description = """ROT13 Encryption module for C++, returns a few version of the provided payload with a C++ decryption function
    """

    def __init__(self, config):

        self.payload = config.get('payload')
        super().__init__(status=True) # set status to True to indicate the module is usable

    def run(self):

        payload_fh = open(self.payload, 'rb')
        payload = payload_fh.read()
        payload_fh.close() 

        payload = bytearray(payload)
        for i in range(0, len(payload)):
            payload[i] = (payload[i] + 13) % 256

        base16EncodedPayload = payload.hex()

        intArray = create_int_string(payload, language="cpp")
        hexArray = create_hex_string(payload, language="cpp")
        
        hexString = "\""
        for i in range(0, len(base16EncodedPayload), 2):
            hexString += "\\x" + base16EncodedPayload[i:i+2]
        hexString += "\";"        


        with open(os.path.join('modules','cpp','rot13','template.cpp')) as fh:
            template = Template(fh.read())
            cpp_code = template.render(
                base16EncodedPayload=lines(base16EncodedPayload, language="cpp"),
                intArray=intArray,
                hexArray=hexArray,
                hexString=hexString,
                payloadSize=len(payload)
            )

        return [{
            'filename': 'cpp_code.cpp',
            'data': cpp_code,
            'type': 'text'
        }, {
            'filename': 'encrypted_payload.bin',
            'data': payload,
            'type': 'binary'
        }]
    

    


from modules.Module import Module
from utils import create_hex_string, create_int_string
from base64 import b64encode 
import os 
from jinja2 import Template 
from utils import lines 

class xor(Module):

    options = {
        'key': { 'desc': 'key to use', 'required': True },
        'payload': { 'desc': 'path to a payload to encrypt', 'required': True },
        'output': { 'desc': 'directory to write files to, otherwise writes to, otherwise writes files to ./output/', 'required': False }
    }

    input_type = "yaml"
    module_type = "payload" # change this to something else

    description = """XOR cipher module for PowerShell, returns a base64, base16 and binary version of the provided payload with a PowerShell decryption function"""

    def __init__(self, config):

        self.key = config.get('key')
        self.payload = config.get('payload')
        super().__init__(status=False) # set status to True to indicate the module is usable

    def run(self):

        payload_fh = open(self.payload, 'rb')
        payload = payload_fh.read()
        payload_fh.close() 

        payload = bytearray(payload)
        bytekey = bytearray(self.key, 'utf-8')
        for i in range(0, len(payload)):
            payload[i] ^= i % len(bytekey)

        base64EncodedPayload = (b64encode(payload)).decode('utf-8')
        base64EncodedXORKey = (b64encode(bytekey)).decode('utf-8')
        base16EncodedPayload = payload.hex()
        base16EncodedXORKey = bytekey.hex()

        intString = create_int_string(payload)
        hexString = create_hex_string(payload)

        with open(os.path.join('modules','powershell','xor','template.ps1')) as fh:
            template = Template(fh.read())
            powershell_code = template.render(
                base64EncodedPayload=lines(base64EncodedPayload, language="powershell"),
                base64EncodedXORKey=lines(base64EncodedXORKey, language="powershell"),
                base16EncodedPayload=lines(base16EncodedPayload, language="powershell"),
                base16EncodedXORKey=lines(base16EncodedXORKey, language="powershell"),
                intArray=intString,
                hexArray=hexString,
                key=self.key,
                xorStringValue=self.key,
                xorIntArray=create_int_string(bytekey),
                xorHexArray=create_hex_string(bytekey)
            )

        return [{
            'filename': 'powershell_code.ps1',
            'data': powershell_code,
            'type': 'text'
        }, {
            'filename': 'encrypted_payload.bin',
            'data': payload,
            'type': 'binary'
        }]
    

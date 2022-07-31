from modules.Module import Module
from misc.utils import create_hex_string, create_int_string
from base64 import b64encode 
import os 
from jinja2 import Template 
from misc.utils import lines 
class xor(Module):

    options = {
        'key': { 'desc': 'key to use', 'required': True },
        'payload': { 'desc': 'path to a payload to encrypt', 'required': True },
        'output': { 'desc': 'directory to write files to, otherwise writes to, otherwise writes files to ./output/', 'required': False }
    }

    input_type = "yaml"
    module_type = "payload" # change this to something else

    description = """XOR cipher module for Visual Basic, returns a base64, base16 and binary version of the provided payload with a VB decryption function
    """

    def __init__(self, config):

        self.key = config.get('key')
        self.payload = config.get('payload')
        super().__init__(status=True) # set status to True to indicate the module is usable

    def run(self):

        payload_fh = open(self.payload, 'rb')
        payload = payload_fh.read()
        payload_fh.close() 

        payload = bytearray(payload)
        bytekey = bytearray(self.key, 'utf-8')

        print(payload.hex())
        for i in range(0, len(payload)):
            payload[i] ^= bytekey[i % len(bytekey)]

        base64EncodedPayload = (b64encode(payload)).decode('utf-8')
        base16EncodedPayload = payload.hex()

        intString = create_int_string(payload, language="visualbasic")
        hexString = create_hex_string(payload, language="visualbasic")

        with open(os.path.join('modules','visualbasic','xor','template.vba')) as fh:
            template = Template(fh.read())
            vba_code = template.render(
                base64EncodedPayload=lines(base64EncodedPayload, language="visualbasic"),
                base16EncodedPayload=lines(base16EncodedPayload, language="visualbasic"),
                intArray=intString,
                hexArray=hexString,
                key=self.key,
                xorStringValue=self.key,
                xorIntArray=create_int_string(bytekey, language="visualbasic"),
                xorHexArray=create_hex_string(bytekey, language="visualbasic"),
                byteCount=int(len(base16EncodedPayload)/2)-1,
                xorByteCount=len(self.key)
            )

        return [{
            'filename': 'vba_code.vba',
            'data': vba_code,
            'type': 'text'
        }, {
            'filename': 'encrypted_payload.bin',
            'data': payload,
            'type': 'binary'
        }]

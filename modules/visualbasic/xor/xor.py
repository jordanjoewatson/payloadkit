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
        super().__init__(status=False) # set status to True to indicate the module is usable

    def run(self):

        payload_fh = open(self.payload, 'rb')
        payload = payload_fh.read()
        payload_fh.close() 

        payload = bytearray(payload)
        bytekey = bytearray(self.key, 'utf-8')
        for i in range(0, len(payload)):
            payload[i] ^= bytekey[i % len(bytekey)]

        base64EncodedPayload = (b64encode(payload)).decode('utf-8')
        base16EncodedPayload = payload.hex()

        intLs = []
        for i in range(0, len(payload), 50):
            intLs.append(','.join([
                str(int(p)) for p in payload[i:i+50]
            ]) + ',')

        # remove the last character because of the trailint ','
        intString = '\n'.join(intLs)[:-1]

        hexLs = []
        for i in range(0, len(payload), 50):
            hexLs.append(','.join([
                str(hex(p)) for p in payload[i:i+50]
            ]) + ',')

        hexString = '\n'.join(hexLs)[:-1]


        with open(os.path.join('modules','visualbasic','xor','template.vba')) as fh:
            template = Template(fh.read())
            vba_code = template.render(
                base64EncodedPayload=lines(base64EncodedPayload, language="visualbasic"),
                base16EncodedPayload=lines(base16EncodedPayload, language="visualbasic"),
                intArray=intString,
                hexArray=hexString,
                key=self.key
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


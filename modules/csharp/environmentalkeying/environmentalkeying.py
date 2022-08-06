from modules.Module import Module
from misc.utils import create_hex_string, create_int_string
from base64 import b64encode 
import os 
from jinja2 import Template 
from misc.utils import lines 

class environmentalkeying(Module):

    options = {
        'key': { 'desc': 'key to use, e.g. username', 'required': True },
        'value': { 'desc': 'value of the key e.g. jord', 'required': True },
        'xorkey': { 'desc': 'key to use for xor\'ing xor key', 'required': True },
        'output': { 'desc': 'directory to write files to, otherwise writes to, otherwise writes files to ./output/', 'required': False }
    }

    input_type = "yaml"
    module_type = "payload" # change this to something else

    description = "Generates an obfuscated function and payload for environment keying"

    def __init__(self, config):

        self.key = config.get('key')
        self.value = config.get('value')
        self.xorkey = config.get('xorkey')
        super().__init__(status=True) # set status to True to indicate the module is usable

    def run(self):

        value = bytearray(self.value, 'utf-8')
        bytekey = bytearray(self.xorkey, 'utf-8')
        for i in range(0, len(value)):
            value[i] ^= bytekey[i % len(bytekey)]

        base64EncodedValue = (b64encode(value)).decode('utf-8')

        with open(os.path.join('modules','csharp','environmentalkeying','template.cs')) as fh:
            template = Template(fh.read())
            cs_code = template.render(
                encoded=base64EncodedValue,
                xorkey=self.xorkey,
                key=self.key,
                byteArrayInt=create_int_string(value),
                byteArrayHex=create_hex_string(value)
            )

        return [{
            'filename': 'csharp_code.cs',
            'data': cs_code,
            'type': 'text'
        }]
    

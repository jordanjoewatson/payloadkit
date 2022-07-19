from modules.Module import Module
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad 
import random 
from string import ascii_letters, digits, punctuation
from base64 import b64encode 
from utils import lines
import os
from jinja2 import Template

"""
Need to add options somehow
"""
class aes(Module):

    options = {
        'blocksize': { 'desc': 'blocksize to use, from AES-256, AES-192, AES-128', 'required': True },
        'payload': { 'desc': 'path to a payload to encrypt', 'required': True },
        'output': { 'desc': 'directory to write files to, otherwise writes to, otherwise writes files to ./output/', 'required': False }
    }

    input_type = "yaml"
    module_type = "payload" # change this to something else

    description = """AES Encryption module for C#, returns a base64, base16 and binary version of the provided payload with a C# decryption function"""

    def __init__(self, config):

        self.blocksize = config.get('blocksize')
        self.payload = config.get('payload')
        super().__init__(status=False) # set status to True to indicate the module is usable

    def get_hashlength(self):
        if self.blocksize == "AES-128":
            return 16
        elif self.blocksize == "AES-192":
            return 24
        elif self.blocksize == "AES-256":
            return 32
        else:
            print("csharp/aes.py: Error invalid blocksize")
            exit()

    def run(self):
        
        payload_fh = open(self.payload, 'rb')
        payload = payload_fh.read()
        payload_fh.close() 

        hashlength = self.get_hashlength()
        characters = ascii_letters+digits+punctuation
        hash = ''.join(random.choices(characters, k=hashlength))
        iv = ''.join(random.choices(characters, k=16))
        bytehash = bytearray(hash, 'utf-8')
        byteiv = bytearray(iv, 'utf-8')

        cipher = AES.new(bytehash, AES.MODE_CBC, byteiv)
        payload = cipher.encrypt(pad(payload, 16))

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

        with open(os.path.join('modules','csharp','aes','template.cs')) as fh:
            template = Template(fh.read())
            csharp_code = template.render(
                base64EncodedPayload=lines(base64EncodedPayload, language="csharp"),
                base16EncodedPayload=lines(base16EncodedPayload, language="csharp"),
                byteArrayInt=intString,
                byteArrayHex=hexString
            )

        # write out an encrypted payload binary
        # write out function data into the cs code containing, base64 encoded payload and arguments with a base64 function
        # a base16 encoded payload and arguments with a base16 function
        # all of these are separated by a ############# line with a comment detailing what's happening

        # pass data back in specific format to be written out to directory
        return [{
            'filename': 'csharp_code.cs',
            'data': csharp_code,
            'type': 'text'
        }, {
            'filename': 'encrypted_payload.bin',
            'data': payload,
            'type': 'binary'
        }]


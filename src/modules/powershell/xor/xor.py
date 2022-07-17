from modules.Module import Module

class xor(Module):

    options = {
        'key': { 'desc': 'key to use', 'required': True },
        'payload': { 'desc': 'path to a payload to encrypt', 'required': True },
        'output': { 'desc': 'directory to write files to, otherwise writes to, otherwise writes files to ./output/', 'required': False }
    }

    input_type = "yaml"
    module_type = "payload" # change this to something else

    description = """XOR cipher module for PowerShell, returns a base64, base16 and binary version of the provided payload with a PowerShell decryption function
    """

    def __init__(self, config):

        self.key = config.get('key')
        self.payload = config.get('payload')
        super().__init__(status=False) # set status to True to indicate the module is usable

    def run(self):
        
        function_string = "test()"
        encrypted_payload = b'11000010'

        # write out an encrypted payload binary
        # write out function data into the cs code containing, base64 encoded payload and arguments with a base64 function
        # a base16 encoded payload and arguments with a base16 function
        # all of these are separated by a ############# line with a comment detailing what's happening

        # pass data back in specific format to be written out to directory
        return [{
            'filename': 'powershell_code.ps1',
            'data': function_string,
            'type': 'text'
        }, {
            'filename': 'encrypted_payload.bin',
            'data': encrypted_payload,
            'type': 'binary'
        }]


from modules.Module import Module
import os
import typer
from misc.utils import create_int_string
"""
Need to add options somehow
"""
class intarray(Module):

    input_type = "string"
    module_type = "query"

    description = """Module that accepts a string argument for a binary. Prints hex array e.g. 0x12, 0x23 ..."""

    def __init__(self, filepath):
        self.filepath = filepath
        super().__init__(status=True) # set status to True to indicate the module is usable


    def run(self):
        with open(self.filepath, 'rb') as fh:
            bs = fh.read()
            hexString = ""

            """
            C hexstring
            for i in range(0, len(bs.hex()), 2):
                hexString += "\\x" + bs.hex()[i:i+2]
            """

            """
            base16 string
            bs.hex()
            """
            print(create_int_string(bs).replace('\n',''))

            
        print(" ")
        return

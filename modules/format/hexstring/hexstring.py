from modules.Module import Module
import os
import typer
from misc.utils import create_hex_string, create_int_string
"""
Need to add options somehow
"""
class hexstring(Module):

    input_type = "string"
    module_type = "query"

    description = """Module that accepts a string argument for a binary. Prints hex array e.g. 0x12, 0x23 ..."""

    def __init__(self, filepath):
        self.filepath = filepath
        super().__init__(status=True) # set status to True to indicate the module is usable


    def run(self):
        with open(self.filepath, 'rb') as fh:
            bs = fh.read()
            print(bs.hex())
            
        print(" ")
        return

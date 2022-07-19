from modules.Module import Module
import yaml
import os
import typer
from utils import load_config

"""
Need to add options somehow
"""
class dllimport(Module):

    input_type = "string"
    module_type = "query"

    description = """Module that accepts a string argument to find a C# DLLImport statement. String argument should be API function name
    """

    def __init__(self, dllimport):
        self.dllimport = dllimport
        super().__init__(status=True) # set status to True to indicate the module is usable


    def run(self):

        dllimport_found = False
        yaml_config = load_config(os.path.join("modules", "csharp", "dllimport", "imports.yaml"))
    
        for dct in yaml_config['import_statements']:
            if dct['api'] == self.dllimport:
                print(dct['import'])
                dllimport_found = True 

        if not dllimport_found:
            print("Error, unable to find DLLImport in module")

        print(" ")
        return


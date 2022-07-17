from modules.Module import Module

"""
Need to add options somehow
"""
class xor(Module):

    options = {
        'key': 'key used to encrypt payload'
    }

    def __init__(self, config):
        
        # self.blocksize = "testing"

        # do assignments here
        #print("WORKING")
        super().__init__(status=False) # set status to True to indicate the module is usable

    

    


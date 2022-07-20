

class Module:

    options = {}
    input_type = None
    description = None

    def __init__(self, status=False):
        self.status = status # used to indicate if it's ready to use

    def check_requirements(self):
        requirements = True

        for name in self.options:

            required = self.options[name]['required']
            if required and not getattr(self, name): # not hasattr(self, name):
                print("  Missing value: " + name)
                requirements = False 
        return requirements

    def help(self):
        for name in self.options:
            print("  option: " + name)
            print("  description: " + self.options[name])
            print('')

    def get_status(self):
        return self.status

    def get_options(self):
        return self.options

    def get_input_type(self):
        return self.input_type

    def get_description(self):
        return self.description
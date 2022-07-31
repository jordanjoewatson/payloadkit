from inspect import modulesbyfile
import typer
from typing import Optional
from importlib import import_module
import re
import os 
from pathlib import Path 
import yaml
import time 
from misc.utils import log, get_time, load_config, check_module, get_output_directory

banner = """
  ┌─┐┌─┐┬ ┬┬  ┌─┐┌─┐┌┬┐┬┌─┬┌┬┐
  ├─┘├─┤└┬┘│  │ │├─┤ ││├┴┐│ │ 
  ┴  ┴ ┴ ┴ ┴─┘└─┘┴ ┴─┴┘┴ ┴┴ ┴

     v1.0 @jordanjoewatson
"""


print(banner)

app = typer.Typer()
languages = ["cpp","csharp","powershell","visualbasic","cobaltstrike"]

@app.command(name="run", help="Runs a module")
def run(module: str, arg: str):

    time_obj = get_time()
    check_module(module)

    language,module = module.split('.')
    Cls = getattr(import_module('modules.{}.{}.{}'.format(
        language, module, module
    )), module) 

    module_input_type = Cls.get_input_type(Cls)

    if module_input_type == "yaml":
        yaml_config = load_config(arg)
        # print(yaml_config)
        cls = Cls(yaml_config)

        if not cls.check_requirements():
            typer.echo(typer.style("[!] Error in check requirements for config {}\n".format(arg), fg=typer.colors.RED, bold=True))
            exit()

        output_directory = get_output_directory(yaml_config, language+'_'+module, time_obj)
        os.mkdir(output_directory)

        log("Running module {} on config {}".format(language+'.'+module, arg), time_obj, logfile=True)
        output_data = cls.run()

        log("Writing out files to: " + output_directory, time_obj, logfile=True)
        for dct in output_data:

            output_type = dct['type']
            file_permissions = "wb" if output_type == "binary" else "w"
            with open(os.path.join(output_directory, dct['filename']), file_permissions) as fh:
                fh.write(dct['data'])

    # string modules used for general querying things
    elif module_input_type == "string":
        cls = Cls(arg)

        if not cls.check_requirements():
            typer.echo(typer.style(f"[!] Error in check requirements\n", fg=typer.colors.RED, bold=True))
            exit()

        log("Running module {} with arg {}\n".format(language+'.'+module, arg), time_obj, logfile=True)
        cls.run()

    else:
        typer.echo(typer.style("[!] Invalid module_input_type for module {}\n".format(language+'.'+module), fg=typer.colors.RED, bold=True))

@app.command(name="ls", help="Lists payloadkit modules")
def ls():

    print("Available modules:")
    for language in languages:
        language_path = os.path.join("modules", language)
        modules = os.listdir(language_path)

        for module in modules:
            Cls = getattr(import_module('modules.{}.{}.{}'.format(
                language, module, module
            )), module) 
            cls = Cls({})
            if cls.get_status():
                print("  {}.{}".format(language, module))
            else:
                print("  {}.{} (incomplete)".format(language, module))

    print("")
    
@app.command(name="info", help="Displays info on module")
def info(module: str):
    check_module(module)

    language,module = module.split('.')
    Cls = getattr(import_module('modules.{}.{}.{}'.format(
        language, module, module
    )), module) 

    cls = Cls({})
    desc = cls.get_description()
    options = cls.get_options()

    print(desc)

    # Maybe change this so it checks the modules input, if "yaml" then fill out config, else "string", provide string arg
    print("Fill out the following yaml file, run with python3 payloadkit.py run {} config.yaml\n".format(language+'.'+module))
    for option in options:
        optional_string = "(Optional) " if not options[option]['required'] else ""
        description_string = options[option]['desc']

        print("  {}: {}{}".format(
            option, optional_string, description_string
        ))

    print(" ")


if __name__ == "__main__":
	app()

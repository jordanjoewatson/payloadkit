import os 
import time 
import re
import typer
import yaml 

def get_time():
    return time.localtime()
    

"""
Writes out string s to output, also writes to log file depending on boolean value
"""
def log(s, time_obj, logfile=False):

    print(s)
    if logfile:
        current_time = time.strftime("%Y/%m/%D %H:%M:%S", time_obj)
        with open("log.txt", "a") as fh:
            fh.write("{}: {}".format(current_time, s))


def load_config(config_filepath):
    try:
        with open(config_filepath) as fh:
            config = yaml.load(fh, Loader=yaml.FullLoader)
            return config
    except:
        typer.echo(typer.style(f"[!] utils.py: Error loading config: {config_filepath}\n", fg=typer.colors.RED, bold=True))
        exit()

def check_module(module):
    if not re.match(r"(csharp|powershell|visualbasic|cobaltstrike|cpp|csharp).[a-zA-Z]+", module):
        print("[!] utils.py: invalid module name, use format <language>.<module>")
        exit()


def get_output_directory(config: str, module: str, time_obj: time.struct_time):
    if not config.get('output'):

        current_time = time.strftime("%H-%M-%S", time_obj)
        return os.path.join('output', module+'_'+current_time)
    return config.get('output')

def lines(l, language):
    if language == "csharp":
        s = ""
        for itr in range(0, len(l), 200):
            if itr > 0:
                s += " +\n"
            s += "\"{}\"".format(l[itr:itr+200])

        return s
    if language == "powershell":
        s = ""
        for itr in range(0, len(l), 200):
            if itr > 0:
                s += "+ "
            s += "\"{}\"`\n".format(l[itr:itr+200])
        
        return s[:-2]
    else:
        print("utils.py: Language not implement yet")
        exit()

def create_int_string(payload):
    intLs = []
    for i in range(0, len(payload), 50):
        intLs.append(','.join([
            str(int(p)) for p in payload[i:i+50]
        ]) + ',')

    # remove the last character because of the trailint ','
    intString = '\n'.join(intLs)[:-1]
    return intString 

def create_hex_string(payload):
    hexLs = []
    for i in range(0, len(payload), 50):
        hexLs.append(','.join([
            str(hex(p)) for p in payload[i:i+50]
        ]) + ',')

    hexString = '\n'.join(hexLs)[:-1]
    return hexString
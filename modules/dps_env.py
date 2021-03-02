##############################################
## Custom DPS Module.
## Name: Aliasing commands.
## Description: Set an alias for a command as defined in ~/.dps/.dpsrc file.
## Author: RackünSec
## Author URL: https://github.com/RackunSec/
## TODO: Set/Update aliases.
##

## REQUIREMENTS:
import re

## Method: show your aliases set in .dpsrc:
def show_alias(session,prompt_ui):
    print(prompt_ui.bcolors['BOLD']+"\n ▿ DPS.ini Defined [ALIASES] ▿ "+prompt_ui.bcolors['ENDC'])
    for alias in session.ALIASES:
        print(f"  ◦ Alias found for {prompt_ui.bcolors['OKGREEN']}{alias}{prompt_ui.bcolors['ENDC']} as '{prompt_ui.bcolors['OKGREEN']}{session.ALIASES[alias]}{prompt_ui.bcolors['ENDC']}'")
    print("")
    return

## Method: define a session variable:
def define_var(cmd,session,prompt_ui):
    if len(cmd.split())==3:
        WARN=prompt_ui.bcolors['WARN']
        ENDC=prompt_ui.bcolors['ENDC']
        BOLD=prompt_ui.bcolors['BOLD']
        OKGREEN=prompt_ui.bcolors['OKGREEN']
        FAIL=prompt_ui.bcolors['FAIL']
        if re.match("^[^:]+:\s+[^\s]+$",cmd): # syntax [ OK ]
            key=cmd.split()[1]
            key=re.sub(":$","",key) # drop the colon
            val=cmd.split()[2]
            print(f"\n ▹ Defining variable {BOLD}{OKGREEN}{key}{ENDC} value {BOLD}{OKGREEN}{val}{ENDC} for this DPS session.\n")
            session.VARIABLES[key]=val
            return
        else:
            print(f"\n{FAIL} ✖ Syntax for \"def\" incorrect. See Below.{ENDC}")
            session.help.msg("def",session,prompt_ui)
    else:
        session.help.msg("def",session,prompt_ui)

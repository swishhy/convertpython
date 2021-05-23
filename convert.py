# Python|Convert .py to .exe
# Made by sw1shhy

# Modules
import os
from time import sleep
from colorama import *
init(convert=True)

# Main functions
print(f"""
 ██████╗ ██████╗ ███╗   ██╗██╗   ██╗███████╗██████╗ ████████╗
██╔════╝██╔═══██╗████╗  ██║██║   ██║██╔════╝██╔══██╗╚══██╔══╝
██║     ██║   ██║██╔██╗ ██║██║   ██║█████╗  ██████╔╝   ██║   
██║     ██║   ██║██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██╔══██╗   ██║   
╚██████╗╚██████╔╝██║ ╚████║ ╚████╔╝ ███████╗██║  ██║   ██║   
 ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝   ╚═╝   
                                 {Fore.MAGENTA}  © sw1shy
    Convert python script into a executable file
    Usage : put the file you want to convert in the
    same directory with the program.
    {Style.RESET_ALL}
""")

inst = input("> Would you like to install the modules? (y/n) ")
if inst == "y":
    print("Installing modules")
    os.system("pip install pyinstaller")
else:
    print("Skipping...")
    sleep(5)

choice = input("> With icon (y/n) ")
if choice == "y":
    fn = input ("> File name : ")
    ic = input("> Icon name : ")
    os.system(f"pyinstaller -F {fn} -i {ic}")
    print("Converted!")
elif choice == "n":
    fn2 = input("> File name : ")
    os.system(f"pyinstaller -F {fn2}")
    print("Converted!")

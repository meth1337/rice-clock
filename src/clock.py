# Libraries
from datetime import datetime  # Using this lib, we will get the current time
from art import tprint  # Using this lib, we will print the time in ASCII signs
from time import sleep  # Using this lib, we will create a delay in updating time
from os import system  # Using this lib, we will clear the terminal after delay to show the current time
from colorama import Fore  # Using this lib, we will change the color of the text in terminal
import sys  # Using this lib, we will use the arguments for using our script

# I'll add colors to variables, it's easier to use
red = Fore.LIGHTRED_EX  # Red color
green = Fore.GREEN  # Green color
blue = Fore.BLUE  # Blue color
pink = Fore.MAGENTA  # Not actually pink but still xD
yellow = Fore.YELLOW  # Yellow color
cyan = Fore.CYAN  # Cyan color
white = Fore.WHITE  # White color (why the fuck i need it)
reset = Fore.RESET  # To return the base color 
# I think there are more colors, but I added the most of it

# Since script moved to new ASCII text lib, there are new opportunities for fonts now:
# You can change the name of font to whitchever you want to use, for now it will be the default one
# You can see preview of all fonts in README

font = "smpoison"  # Default, you can change the name to switch the font

def clock(color):  # Defining a function
    print(color)  # Changing current terminal font color to chosen color
    system("clear")  # Clearing the terminal
    while True:  # Creating a loop, that repeats itself forever (until it's stopped by user)
        system("clear")  # Clearing the terminal to update the time
        tprint(datetime.now().strftime("%H:%M:%S"), font=font)  # Printing the time
        sleep(1)  # Making a delay in 1 second

try:  # Opens try block to run the script options and work with issues below
    # Working with arguments
    if sys.argv[1] == "-r":  # Runs script with red color
        clock(color=red)
    elif sys.argv[1] == "-g":  # Runs script with green color
        clock(color=green)
    elif sys.argv[1] == "-b":  # Runs script with blue color
        clock(color=blue)
    elif sys.argv[1] == "-p":  # Runs script with pink color
        clock(color=pink)
    elif sys.argv[1] == "-y":  # Runs script with yellow color
        clock(color=yellow)
    elif sys.argv[1] == "-c":  # Runs script with cyan color
        clock(color=cyan)
    elif sys.argv[1] == "-w":  # Runs script with cyan color
        clock(color=white)
    elif sys.argv[1] == "-h" or "--help":  # Help argument (Returns info on how to use the script)
        print("A rice-like clock for terminals.\nFor usage, enter the command rice-clock + color, that you want to use\nAvailable colors:\n - r - red\n - g - green\n - b - blue\n - p - pink\n - y - yellow\n - c - cyan\n - w - white\n\nrice-clock homepage: https://github.com/meth1337/rice-clock\nReport bugs to https://github.com/meth1337/rice-clock/issues")
except IndexError:  # If no arguments were entered (returns help argument value)
    print("A rice-like clock for terminals.\nFor usage, enter the command rice-clock + color, that you want to use\nAvailable colors:\n - r - red\n - g - green\n - b - blue\n - p - pink\n - y - yellow\n - c - cyan\n - w - white\n\nrice-clock homepage: https://github.com/meth1337/rice-clock\nReport bugs to https://github.com/meth1337/rice-clock/issues")
except KeyboardInterrupt:  # If script was stopped by user
    print(reset)  # Resets the font color
    system("clear")
    exit()
except:  # Except block for issues
    print(f"{red}Error!{reset}")
    exit()
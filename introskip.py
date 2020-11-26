#!/usr/bin/python
# Customizable Intro Skipper for VLC
from pyautogui import press
from time import sleep
from math import floor
from config import intro_duration
import sys
import os

# This fucntion only works in UNIX
def addToBashrc():
    location=__file__ # Grabs the absolute path of the script.
    os.system(f"chmod u+x {location}") # Makes the script executable
    os.system(f"echo alias skip=\"{location}\" >> ~/.bashrc") # Saves an alias pointing to the script
    os.system('#!/usr/bin/env bash \n source ~/.bashrc') # Starts a shell, and forces the bashrc file to be reloaded


def skip(skips):
    # Volume down (Static value of 4 presses)
    for _ in range(0,4):
        press('down')
        sleep(0.05)
    # Skip ahead in 10 second chunks
    for _ in range(0,skips):
        press('right')
        sleep(0.05)
    # Volume up  (Static value of 4 presses)
    for _ in range(0,4):
        press('up')
        sleep(0.05)


try:
    # This catches the 'add' argument, if no argument
    # is given, the Exception is caught.
    arg=sys.argv[1]
    if arg == 'add':
        addToBashrc()
except Exception:
    # VLC arrow skips are 10 seconds
    # Here we divide intro length by 10.
    # Taking the floor, to come up with
    # the number of skips
    try:
        number_of_skips=floor(intro_duration/10)
        skip(number_of_skips)
    except Exception as exc:
        print(exc)

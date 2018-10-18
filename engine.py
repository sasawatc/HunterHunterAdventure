import re
import sys
import time

import colorama

"""
@author: sasawat.chanate
"""

"""
DocString:

    This file contains functions and constants related to the behavior of the game.
"""

PRINT_SPEED = 0.05  # default 0.05
SCRIPT_LINE_SPEED = 0.9  # default 0.9
PRINT_INSTANT = 0  # default 0
PAUSE_DURATION = 0.5  # default 0.5
DIGITS_ONLY = r"^\d+$"
ALPHABET_ONLY = r"^[a-z]+$"
EVERYTHING = r".*?"


# ScriptLine = namedtuple("ScriptLine", "name, text")
# Delay = seconds

def delay_print(text="", delay=0):
    for i in text:
        time.sleep(delay)
        print(i, end='')
        sys.stdout.flush()


def game_print(text, color=colorama.Style.RESET_ALL, delay=PRINT_SPEED, end="\n", form_feed=False):
    colorama.init()
    if form_feed:  # if form_feed is True, then performs form feed
        form_feed()

    # Windows's CLI doesn't support color and styling
    if sys.platform == "win32":
        delay_print(text + end, delay)
    else:
        delay_print(color + text + end + colorama.Style.RESET_ALL, delay)


def script_print(script):
    for line in script:
        game_print(str(line), delay=PRINT_INSTANT)
        pause(SCRIPT_LINE_SPEED)


def game_input(text=">>> ", regex=EVERYTHING, color=colorama.Fore.RED, begin="\n", end=""):
    while True:
        game_print(begin, end="")
        game_print(text=text, color=color, end=end, delay=PRINT_INSTANT)
        input_ = input()
        if re.match(regex, input_):
            break
        else:
            game_print("INVALID INPUT: Please try again!", color=colorama.Fore.RED + colorama.Style.BRIGHT,
                       delay=PRINT_INSTANT)
    return input_


def pause(delay):
    time.sleep(delay)


def system_pause():
    input("\nPress the <ENTER> key to continue...")


def form_feed():
    colorama.init()  # attempt to convert ASCII code for specific OS (especially for Windows)
    print("\f", end='')  # intended for IDE consoles
    print("\x1B[2J")  # intended for Terminal CLI


def fail(msg=""):
    game_print(f"\nGAME OVER: {msg}", color=colorama.Fore.RED + colorama.Style.BRIGHT)
    system_pause()
    sys.exit()

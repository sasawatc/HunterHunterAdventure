import re
import sys
import time

from fg_color import *

PRINT_SPEED = 0  # default 0.05
PRINT_INSTANT = 0
PAUSE_DURATION = 0.5
DIGITS_ONLY = r"^\d+$"
ALPHABET_ONLY = r"^[a-z]+$"
EVERYTHING = r".*?"


# Question = namedtuple("Question", "question, choices, user_selection")
# Delay = seconds


def delay_print(text, delay=0):
    for i in text:
        time.sleep(delay)
        print(i, end='')
        sys.stdout.flush()


def game_print(text, color=FgColor.END, delay=PRINT_SPEED, end="\n"):
    delay_print(color + text + end + FgColor.END, delay)


def game_input(text=">>> ", regex=EVERYTHING, color=FgColor.RED, begin="\n", end=""):
    while True:
        game_print(begin, end="")
        game_print(text=text, color=color, end=end)
        input_ = input()
        if re.match(regex, input_):
            break
        else:
            game_print("INVALID INPUT: Please try again!", color=FgColor.ERR)
    return input_


def pause(delay):
    time.sleep(delay)


def form_feed():
    if sys.platform == 'win32':
        from colorama import init
        init()
    print("\x1B[2J")
    print("\f", end='')

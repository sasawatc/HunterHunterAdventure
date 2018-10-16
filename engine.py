import sys
import time

from fg_color import *

# from script_reader import *

PRINT_SPEED = 0  # default 0.05
PRINT_INSTANT = 0
PAUSE_DURATION = 0.5


# Delay = seconds


def delay_print(text, delay=0):
    for i in text:
        time.sleep(delay)
        print(i, end='')
        sys.stdout.flush()


def game_print(text, color=FgColor.END, delay=PRINT_SPEED, end="\n"):
    delay_print(color + text + end + FgColor.END, delay)


# def script_print(script):
#     color = FgColor.END
#     delay = PRINT_SPEED
#
#     delay_print()

def pause(delay):
    time.sleep(delay)

import sys
import time

from fg_color import *

PRINT_SPEED = 0.05
PRINT_INSTANT = 0
PAUSE_DURATION = 0.5


# Delay = seconds


def delay_print(text, delay=0):
    for i in text:
        time.sleep(delay)
        print(i, end='')
        sys.stdout.flush()


def game_print(text, color=FgColor.END, delay=PRINT_SPEED):
    delay_print(color + text + FgColor.END, delay)


def pause(delay):
    time.sleep(delay)

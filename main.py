from engine import *


def start_game():
    delay_print("""Fearsome monsters... Exotic creatures...
Vast riches... Hidden treasures...
Evil enclaves... Unexplored lands...
The word "unknown" holds magic.
And some incredible people are drawn to that magic.\n""")
    game_print("They are known as... ")
    pause(PAUSE_DURATION)
    game_print("Hunters!\n", FgColor.BOLD, PRINT_INSTANT)


def main():
    start_game()


if __name__ == "__main__":
    main()

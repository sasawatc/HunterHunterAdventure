from greet_player import *

player_name = "DefaultName"


def start_game():
    # self._start_prologue()
    greet_player()


def start_prologue():
    game_print("""
Fearsome monsters... Exotic creatures...
Vast riches... Hidden treasures...
Evil enclaves... Unexplored lands...
The word "unknown" holds magic.
And some incredible people are drawn to that magic.""")
    game_print("They are known as... ", end="")
    pause(PAUSE_DURATION)
    game_print("Hunters!", color=FgColor.BOLD, delay=PRINT_INSTANT)


def main():
    start_game()


if __name__ == "__main__":
    main()

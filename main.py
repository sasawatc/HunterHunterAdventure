from gameplay import *

"""
Created on Tue Oct 9 01:39:00 2018

@author: sasawat.chanate
"""

"""
DocString:

    A) Introduction:
    This is a text adventure game based on a Japanese animation TV series, Hunter × Hunter (2011)
    which was based on Yoshihiro Togashi's Hunter × Hunter manga.
    The game consists of multiple scenario choice questions and fun mini-games.
    Please be aware, you might need more than skills to beat the game. Please do not be discourage if
    you happen to lose in the first trial.
    
    Note:
    The content might be a different from the original series to serve requirement purposes.

    B) Known Bugs and/or Errors:
    
    >>>Windows<<<
    - Unable to manipulate color and styling to printed text due to Windows not compiling the ANSI standards
    - Colorama failed to mitigrate this issue (current implementation disables styling for win32 system)
    
    >>>macOS<<<
    - Unknown (no hardware for rigorous testing)

"""


def start_prologue():
    game_print("\nFearsome monsters... Exotic creatures...")
    game_print("Vast riches... Hidden treasures...")
    game_print("Evil enclaves... Unexplored lands...")
    game_print("The word \"unknown\" holds magic.")
    game_print("And some incredible people are drawn to that magic.")
    game_print("They are known as... ", end="")
    pause(PAUSE_DURATION)
    game_print("Hunters!", delay=PRINT_INSTANT)
    system_pause()


def goodbye():
    game_print("\n...to be continued...")
    game_print("Looks like that is all we got for this episode.")
    game_print("I hope you enjoyed it after all this is just 2/148 episodes of the show.")
    game_print("If you would like to know how the story continue, feel free to watch")
    game_print("the full show.")
    game_print("Lastly, I would like to say that all the rights to the story")
    game_print("belongs to the original author, Yoshihiro Togashi. The story used in this")
    game_print("program is solely for educational propose.")
    game_print()
    game_print("Thanks and bye!")
    system_pause()


def main():
    form_feed()
    start_prologue()
    greet_player()
    start_game()
    goodbye()


if __name__ == "__main__":
    main()

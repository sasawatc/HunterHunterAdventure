from engine import *


def ask_name():
    query_loop_count = 0
    last_ans = ""
    # game_print("")
    # game_print("First, what is your name?")
    # game_print("1)\tPETER")
    # game_print("2)\tPAUL")
    # game_print("3)\tMARY")
    # game_print("")
    # game_print("Or just type in your name...")
    # game_print("")
    # game_print(">>> ", color=FgColor.RED, end="")
    # ans = input().upper()

    question = Question(question="First, what is your name?",
                        choices=["1)\tPETER",
                                 "2)\tPAUL",
                                 "3)\tCHASE",
                                 "4)\tNEW NAME"],
                        user_selection="")
    game_print(str(question))

    question.user_selection = game_input(regex=r"^[1-4]$")

    print(question.user_selection)

    # while ans == "1" or ans == "2" or ans == "3":
    #     if ans != last_ans:
    #         game_print("Come on, don't be lazy. Think of your own name.")
    #     else:
    #         game_print(f"Oh! I'm sorry, so you are really are {ans}")
    #     query_loop_count += 1


def greet_player():
    game_print("Hello there! Welcome to the world of Hunters! My name is Ham! I am one of the pro hunters.")

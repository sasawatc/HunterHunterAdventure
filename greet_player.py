from engine import *
from question import Question

"""
@author: sasawat.chanate
"""

"""
DocString:

    This file contains functions related to welcoming player to the game.
    
    Actually, it's trying to reference the humor from the beginning of a Pokemon game.
    Please do try to get it... ToT
"""


def ask_name():
    last_input = ""

    question = Question(question="What is your name?",
                        choices=["1)\tPETER",
                                 "2)\tPAUL",
                                 "3)\tMARY",
                                 "4)\tCHASE",
                                 "5)\tENTER NEW NAME"])
    choice_dict = {'1': "PETER", '2': "PAUL", '3': "MARY", '4': "CHASE", '5': "ENTER NEW NAME"}

    game_print("First things first...")
    while True:
        game_print(str(question))
        question.user_input = game_input(regex=r"^[1-5]$")

        if question.user_input in ['1', '2', '3']:
            if question.user_input != last_input:
                game_print("Come on, don't be lazy!\nThink of your own name!")
                last_input = question.user_input
            else:
                game_print(f"Oh! I'm sorry, so you are really are {choice_dict[question.user_input]}!\nWelcome to the "
                           f"game!!!")
                name = choice_dict[question.user_input]
                break

        elif question.user_input == '4':
            game_print(f"Oh, hi {choice_dict[question.user_input]}!\nIt's an honor to have you try out the game!!!")
            name = choice_dict[question.user_input]
            break

        else:
            game_print(f"Oh, hi {choice_dict[question.user_input]}!"
                       f"\nWhat a weird name?!\nAnyway, welcome to the game!!!")
            name = choice_dict[question.user_input]
            break

    return name


def ask_boy_girl():
    question = Question(question="Remind me, are you a BOY or a GIRL?",
                        choices=["1)\tBOY",
                                 "2)\tGIRL"])
    game_print(str(question))
    question.user_input = game_input(regex=r"^[1-2]$")

    return question.user_input


def print_logo():  # unused
    file = open("artworks/hunter_logo.txt")
    for i in file:
        print(i)


def intro(name):
    game_print(f"Thank you {name} for spending time giving your information to a stranger,")
    game_print("not to mentioned this is merely a computer program. However, in this game,")
    game_print("you'll be adventuring in the world of \"Hunters\" as GON FREECSS,")
    game_print("a twelve years old boy living in a small island called Whale Island.")
    game_print("You are absolutely determined to pass the Hunter Exam and become")
    game_print("one of the hunters to find your mysterious dad, GING FREECSS, which is also a hunter.")
    game_print("Let's start...")


def greet_player():
    form_feed()
    game_print("Hello there!\nWelcome to the world of Hunters!\nMy name is Ham!\nI am one of the pro hunters.\n")
    system_pause()
    form_feed()
    name = ask_name()
    system_pause()
    form_feed()
    gender = ask_boy_girl()  # Intentionally, did not use it was simply for a joke...
    form_feed()
    intro(name)
    system_pause()
    form_feed()

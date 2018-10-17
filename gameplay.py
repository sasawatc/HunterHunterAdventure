import random

from greet_player import *
from question import Question
from script_line import ScriptLine

"""
@author: sasawat.chanate
"""

"""
DocString:

    This file contains main flow of the actual gameplay.
"""


def catch_fish_hi_lo_game():
    ans = random.randint(1, 100)
    attempts_left = 10

    game_print("\nLet's help Gon catch the Lord of the Lake fish!")
    game_print("The game is a simple hi-lo game.")
    game_print("You are supposed to guess the number that the Lord of the Lake had in mind.")
    game_print("For each attempt, the Lord of the Lake will tell you if your guess was too HIGH or too LOW.")
    game_print(f"You have a total of {attempts_left} attempts!")

    while True:
        guess = int(game_input("Guess an integer (1–100): ", regex=r"^(100|[1-9][0-9]?)$"))

        if guess > ans:
            game_print("HI")
        elif guess == ans:
            game_print("Correct")
            break
        else:
            game_print("LO")

        attempts_left -= 1

        if attempts_left < 0:
            fail("Wild Lord of the Lake fled!")
        else:
            game_print(f"Attempts Left: {attempts_left}")

    game_print("\nYou've caught the Lord of the Lake!!!")


def rock_paper_scissors():
    # Player = Gon
    # Com = Leorio

    player_score = 0
    com_score = 0
    wins_required = 3

    game_print("\nIn order to choose which path to go,")
    game_print("Leorio and you decided to have a Rock-Paper-Scissors match.")
    game_print(f"Whoever wins {wins_required} time(s) first get to choose the path they all will proceed.")

    question = Question(question="Rock! Paper! Scissors!",
                        choices=["1)\tRock",
                                 "2)\tPaper",
                                 "3)\tScissors"])
    rps_dict = {1: "Rock", 2: "Paper", 3: "Scissors"}

    while player_score < wins_required and com_score < wins_required:
        print(str(question))
        player = int(game_input(regex=r"^[1-3]$"))

        com = random.randint(1, 4)

        player = rps_dict[player]
        com = rps_dict[com]

        if player == com:
            game_print("Tie!")
        elif player == "Rock":
            if com == "Paper":
                game_print("You lose... " + com + " covers " + player)
                com_score += 1
            else:
                game_print("You win... " + player + " smashes " + com)
                player_score += 1
        elif player == "Paper":
            if com == "Scissors":
                game_print("You lose... " + com + " cut " + player)
                com_score += 1
            else:
                game_print("You win... " + player + " covers " + com)
                player_score += 1
        else:
            if com == "Rock":
                game_print("You lose... " + com + " smashes " + player)
                com_score += 1
            else:
                game_print("You win... " + player + " cut " + com)
                player_score += 1

        game_print(f"Gon: {player_score}")
        game_print(f"Leorio: {com_score}")

        if player_score >= wins_required:
            game_print("\nCongratulations! You win!")
            return "Gon Wins"
        if com_score >= wins_required:
            game_print("\nSorry! You lose!")
            return "Leorio Wins"


def start_game():
    script = [ScriptLine("A", "Gon is still trying to catch the Lord of the Lake?"),
              ScriptLine("Mito", "Huh? Y-Yes... He's been at it for a week."),
              ScriptLine("A", "What a fool!"),
              ScriptLine("A", "Five adults couldn't manage to reel in that monster."),
              ScriptLine("A", "How is a child supposed to catch that beast?"),
              ScriptLine("A", "Mito-san doesn't want him taking the Hunter Exam."),
              ScriptLine("B", "But Gon's old man was the same age when he caught it..."),
              ScriptLine("A", "He can't do it!")]

    script_print(script)
    system_pause()

    # Start catch fist game
    catch_fish_hi_lo_game()
    system_pause()

    script = [ScriptLine("Gon", "Got him!"),
              ScriptLine("Gon", "Yes! Yes! Yes! Yes! Yes!"),
              ScriptLine("Gon", "I got him good!"),
              ScriptLine("A", "It's huge!"),
              ScriptLine("B", "This is the Lord of the Lake?"),
              ScriptLine("C", "It's been twenty years!"),
              ScriptLine("D", "I know! It was Gon's father that time right?"),
              ScriptLine("B", "Gon actually caught the Lord! Look Mito-san!"),
              ScriptLine("Gon", "Mito-san!	I caught the Lord of the Lake as promised..."),
              ScriptLine("Gon", "So I can take the Hunter Exam right? Right?"),
              ScriptLine("Mito", "You really are Ging's son..."),
              ScriptLine("Mito", "Just promise that you'll come back safe. Can you do that?"),
              ScriptLine("Gon", "Uh-huh! I promise!"),
              ScriptLine("Both", "Pinky swear made..."),
              ScriptLine("Both", "Whoever breaks their promise has to swallow a thousand needles."),
              ScriptLine("Both", "Sealed with a kiss!")]

    script_print(script)
    system_pause()

    game_print("\nSoon later, Gon got on a ship filled with the other hunter applicants.")
    game_print("The boat supposedly goes to the exam site.")
    game_print("As the boat went off sea, Gon explored around the ship and made friend")
    game_print("with a clumsy sailor, Katsuo.")
    game_print("However, while onto a long journey, the ship got hit by a gigantic storm...")

    system_pause()

    script = [ScriptLine("A", "Captain! L-Look..."),
              ScriptLine("Katsuo", "If we get caught by that waterspout, the ship will sink!"),
              ScriptLine("Captain", "Lower the sails now."),
              ScriptLine("Katsuo", "Aye!"),
              ScriptLine("Gon", "I'll help!"),
              ScriptLine("Katsuo", "Uh-huh! Come with me!"),
              ScriptLine("Captain", "I'll take the helm. Full to starboard!"),
              ScriptLine("Narrator", "The storm was so strong, it sent Katsuo flying into the sea!"),
              ScriptLine("Gon", "Katsuo-san!")]

    script_print(script)
    system_pause()

    question = Question(question="Katsuo, the sailor, was sent off the ship by the storm.\n"
                                 "What will you do?",
                        choices=["1)\tCall for help",
                                 "2)\tTrust that he can survive; he's a sailor!",
                                 "3)\tJump out of the ship to save him"])

    game_print(str(question))
    question.user_input = game_input(regex=r"^[1-3]$")

    if question.user_input == "1":
        script_print([ScriptLine("Gon", "Help! Help! Help!")])
        game_print("Gon tried to call for help but nobody hears him in the midst of the storm.")
        game_print("Within a flash, Katsuo vanished into the rough sea...")
        game_print("The Captain feels that Gon is not capable of being a hunter.")
        fail("The Captain disqualifies Gon from being a hunter.")

    elif question.user_input == "2":
        game_print("Soon after the storm passes by, you arrived at an island.")
        game_print("However, soon you hear a loud cracking noise."
                   "Turns out, you were deserted in an island with an active volcano."
                   "The Captain laugh as he soon sailing off, \"a life for a life...\"")
        fail("You died in the volcanic island.")
    else:
        script_print([ScriptLine("Gon", "Katsuo-san!")])
        game_print("You scream as you leap out of the deck and grab Katsuo mid-air.")
        game_print("Two of the applicants was around and they quickly grab your two legs"
                   "while holding on to the deck.")
        game_print("You saved Katsuo!")
        game_print("You gained two new friends: Leorio and Kurapika")
        game_print("The Captain praises you and promised you to bring you three to the port"
                   "closest to the exam site!")

    system_pause()

    game_print("After winning the Captain's favor, the trio of Gon, Kurapika, and Leorio arrived safely "
               "at Dolle Harbor near the exam site. After everyone went down from the ship,"
               "the Captain approaches them.")

    script = [ScriptLine("Gon", "Thanks Captain! I had a great time!"),
              ScriptLine("Captain", "I had fun too."),
              ScriptLine("Captain", "Right! As a token of my appreciation, I'll give you some advice."),
              ScriptLine("Gon", "Advice?"),
              ScriptLine("Captain", "Look. See that big cedar tree on the hilltop?"),
              ScriptLine("Captain", "You should make your way there first."),
              ScriptLine("Captain", "It's a shortcut to the exam site."),
              ScriptLine("Gon", "A shortcut? Got it! So I just need to head for that tree!"),
              ScriptLine("Gon", "Thanks"),
              ScriptLine("Captain", "Best of luck!")]

    system_pause()
    script_print(script)
    system_pause()

    game_print("Gon then went on to discuss with Leorio and Kurapika. Leorio, however, argue"
               "that the notice he received mentioned that the exam is supposedly being held"
               "somewhere in Zaban City. Not trusting the Captain, Leorio suggested that "
               "they all could get a bus to Zaban.")
    game_print("Gon disagrees because he think that the Captain would not lie about it.")

    system_pause()
    winner = rock_paper_scissors()
    system_pause()

    if winner == "Gon Wins":
        question = Question(question="Choose a path to go to the exam site...",
                            choices=["1)\tTrust Captain and proceed to the big cedar tree",
                                     "2)\tTrust Leorio and get on the bus to Zaban City"])
        question.user_input = int(game_input(regex=r"^[1-2]$"))

        if question.user_input == 1:
            game_print("You decided to trust the Captain and proceed to the big cedar tree!")
        else:
            game_print("You decided to trust your friend and get on the bus to Zaban City.")
    else:
        question.user_input = random.randint(1, 2)  # Simulate Leorio making a decision

        if question.user_input == 1:
            game_print("Leorio decided to trust you and proceed to the big cedar tree!")
        else:
            game_print("Leorio insisted on getting on the bus to Zaban City.")

    if question.user_input == 1:
        game_print("You found the examination guides that will lead you to the exam site.")
    else:
        fail("It's a TRAP! The bus took a detour into a minefield. You are now dead.")

    system_pause()
    form_feed()

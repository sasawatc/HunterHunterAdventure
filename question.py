"""
@author: sasawat.chanate
"""

"""
DocString:

    Question is a template for questions that will be use in the game.
    Contains strings of questions, choices, and user_input.
"""


class Question:
    def __init__(self, question, choices=None, user_input=None):
        self.question = question
        self.choices = choices
        self.user_input = user_input

    def get_choices_str(self):
        return "\n".join(self.choices)

    def __str__(self):
        return "\n" + self.question + "\n\n" + self.get_choices_str()

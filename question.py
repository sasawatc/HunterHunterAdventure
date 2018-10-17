class Question:
    def __init__(self, question, choices, user_selection):
        self.question = question
        self.choices = choices
        self.user_selection = user_selection

    def get_choices_str(self):
        return "\n".join(self.choices)

    def __str__(self):
        return self.question + "\n" + self.get_choices_str()

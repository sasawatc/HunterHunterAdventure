"""
@author: sasawat.chanate
"""

"""
DocString:

    ScriptLine is a template for each line of a script.
    Contains name of the character and their line.

"""


class ScriptLine:
    def __init__(self, name, text):
        self.name = name
        self.text = text

    def __str__(self):
        return '{:<10s}{:>s}'.format(self.name + ':', self.text)

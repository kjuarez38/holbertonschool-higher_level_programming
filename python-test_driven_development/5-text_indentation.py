#!/usr/bin/python3
"""Square class"""


def text_indentation(text):
    """Prints a text with 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for char in text:
        if char in [".", "?", ":"]:
            print(char, end='\n\n')
        else:
            print(char, end='')

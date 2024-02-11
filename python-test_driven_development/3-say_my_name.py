#!/usr/bin/python3
"""Say my name"""


def say_my_name(first_name, last_name=""):
    """Prints a formatted string with the first and last name"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {first_name}{space}{last_name}".format(
        first_name=first_name,
        space=" " if last_name else "",
        last_name=last_name
    ))

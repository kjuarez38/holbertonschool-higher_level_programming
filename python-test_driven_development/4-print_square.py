#!/usr/bin/python3
"""Print square module"""


def print_square(size):
    """Print square function"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
    
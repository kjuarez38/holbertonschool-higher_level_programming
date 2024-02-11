#!/usr/bin/python3
"""Add integer module"""


def add_integer(a, b=98):
    """Add integer function"""
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        return int(a) + int(b)

    except Exception as e:
        return e

if __name__ == "__main__":
    import doctest
    doctest.testmod()

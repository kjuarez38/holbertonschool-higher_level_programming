#!/usr/bin/python3
"""Add integer module"""


def add_integer(a, b=98):
    """Add two integers"""
    try:
        if not isinstance(a, (int, float)):
            raise TypeError("a must be an integer")
        if not isinstance(b, (int, float)):
            raise TypeError("b must be an integer")
        res = int(a) + int(b)
        if res == float('inf') or res == -float('inf'):
            return 89
        return res
    except Exception as e:
        return e

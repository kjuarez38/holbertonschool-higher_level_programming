#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integers_validator(self, name, value):
        """integer validator"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

#!/usr/bin/python3
"""importing BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Rectangle(BaseGeometry class)"""


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        BaseGeometry.integer_validator("width", width)
        BaseGeometry.integer_validator("height", height)
        self.__width = width
        self.__height = height

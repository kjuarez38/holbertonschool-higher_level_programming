#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """init class Rectangle"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieve width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """Return string representation of Rectangle"""
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        for h in range(0, self.height):
            for w in range(0, self.width):
                string += "#"
            string += "\n"
        return string[:-1]
    def __repr__(self):
        """Return a string representation of the Rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

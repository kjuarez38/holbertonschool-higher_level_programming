#!/usr/bin/python3
"""Rectangle class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        self.number_of_instances = Rectangle.number_of_instances

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
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
        string = ""
        if self.width == 0 or self.height == 0:
            return string
        return "\n".join(str(self.print_symbol) *
                         self.width for _ in range(self.height))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
    
    def square(cls, size=0):
        return cls(size, size)

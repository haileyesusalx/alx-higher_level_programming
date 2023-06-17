#!/usr/bin/python3
"""class rectangle"""


class Rectangle:
    """new class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    """width"""
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    """height"""
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    """area"""
    def area(self):
        return self.width * self.height

    """perimeter"""
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    """str"""
    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        else:
            return "\n".join(["#" * self.width] * self.height)

    """repr"""
    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    """del"""
    def __del__(self):
        print("Bye rectangle...")

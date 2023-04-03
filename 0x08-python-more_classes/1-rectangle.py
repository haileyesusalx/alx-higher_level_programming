#!/usr/bin/python3
""" Rectangle class with width and height """


class Rectangle:
    """ Rectangle class """

    def __init__(self, width=0, height=0):
        """ Initializes a new Rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width of the Rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for the width of the Rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ Height of the Rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for the height of the Rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

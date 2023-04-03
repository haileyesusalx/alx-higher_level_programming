#!/usr/bin/python3
""" Rectangle class with width and height """


class Rectangle:
    """ retrive value at new class crated """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    """ define width of rectangle """
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

    """ define height of rectangle """
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value
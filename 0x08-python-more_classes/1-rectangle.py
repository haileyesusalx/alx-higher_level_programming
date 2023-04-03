#!/usr/bin/python3
""" defines a rectangle class"""


class Rectangle:
    """ new class crated """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    """ represent a rectangle width """
    @property
    def width(self):
        return self.__width

    """ represent a rectangle width for a value"""
    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("ValueError")

        """ represent a rectangle height """
    @property
    def height(self):
        return self.__height

    """ represent a rectangle height at a value """
    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("ValueError")


""" represent formated print"""


def __repr__(self):
    return "{'_Rectangle__height': %d, '_Rectangle__width': %d}" % \
            (self.__height, self.__width)

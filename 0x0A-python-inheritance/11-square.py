#!/usr/bin/python3
"""Module documentation"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class documentation"""
    def __init__(self, width, height):
        """Method documentation"""
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method documentation"""
        return self.__width * self.__height

    def __str__(self):
        """Method documentation"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Class documentation"""
    def __init__(self, size):
        """Method documentation"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Method documentation"""
        return "[Square] {}/{}".format(self.__size, self.__size)

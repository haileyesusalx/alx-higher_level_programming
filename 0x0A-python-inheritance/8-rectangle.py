#!/usr/bin/python3
""" module 8-rectangle.py"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Instantiation of the rectangle."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Returns string representation of the object."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    @property
    def width(self):
        """Returns the width of the rectangle."""
        return self.__width

    @property
    def height(self):
        """Returns the height of the rectangle."""
        return self.__height

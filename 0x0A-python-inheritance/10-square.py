#!/usr/bin/python3
"""Module defining the Square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class representing a square, which inherits from Rectangle"""
    def __init__(self, size):
        """Initialize a new Square instance

        Args:
            size (int): The size of the square
        """
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the string representation of the square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """Compute the area of the square"""
        return self.__size ** 2

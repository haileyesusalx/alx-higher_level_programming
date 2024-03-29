#!/usr/bin/python3
"""
Module 8-rectangle
Defines a rectangle based on 7-rectangle.py
"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Deletes an instance of a rectangle"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """Returns a printable string representation of a rectangle"""

        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.width
                          for i in range(self.height)])

    def __repr__(self):
        """Returns a rectangle that can be used to create a new instance"""

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    @property
    def width(self):
        """Returns the width of a rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of a rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a rectangle"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of a rectangle"""

        return self.width * self.height

    def perimeter(self):
        """Computes the perimeter of a rectangle"""

        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

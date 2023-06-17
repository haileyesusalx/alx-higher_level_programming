#!/usr/bin/python3
"""
Defines a Rectangle class
"""


class Rectangle:
    """
    Rectangle class

    Attributes:
        number_of_instances: number of rectangle instances
        print_symbol: symbol used for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new instance of the Rectangle class

        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Getter for the width of the rectangle

        Returns:
            The width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the width of the rectangle

        Args:
            value (int): the new width value

        Raises:
            TypeError: If the new width value is not an integer
            ValueError: If the new width value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the height of the rectangle

        Returns:
            The height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the height of the rectangle

        Args:
            value (int): the new height value

        Raises:
            TypeError: If the new height value is not an integer
            ValueError: If the new height value is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Computes the area of the rectangle

        Returns:
            The area of the rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Computes the perimeter of the rectangle

        Returns:
            The perimeter of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle

        Returns:
            A string representation of the rectangle
        """

        if self.__width == 0 or self.__height == 0:
            return ""
        s = []
        for i in range(self.__height):
            s.append(str(self.print_symbol) * self.__width)
            if i != self.__height - 1:
                s.append("\n")
        return "".join(s)

    def __repr__(self):
        """
        Returns a string representation of the rectangle that
        can be used to create a new instance of the class

        Returns:
            A string representation of the rectangle
        """

        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Deletes an instance of the Rectangle class
        """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

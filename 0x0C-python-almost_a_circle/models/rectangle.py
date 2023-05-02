#!/usr/bin/python3
"""Module containing the Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Class representing a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor for Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        self.__check_valid_width(value)
        self.__width = value

    def __check_valid_width(self, width):
        """Check if width is valid"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__check_valid_height(value)
        self.__height = value

    def __check_valid_height(self, height):
        """Check if height is valid"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        self.__check_valid_x(value)
        self.__x = value

    def __check_valid_x(self, x):
        """Check if x is valid"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        self.__check_valid_y(value)
        self.__y = value

    def __check_valid_y(self, y):
        """Check if y is valid"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Print the rectangle using '#'"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Update the rectangle"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle"""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}


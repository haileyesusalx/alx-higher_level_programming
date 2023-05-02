#!/usr/bin/python3
"""Rectangle module."""
from models.base import Base


class Rectangle(Base):
    """Define a Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance with '#' characters."""
        print('\n' * self.y, end='')
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Return a string representation of the Rectangle instance."""
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args):
        """Update the Rectangle instance attributes."""
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            elif i == 1:
                self.width = arg
            elif i == 2:
                self.height = arg
            elif i == 3:
                self.x = arg
            elif i == 4:
                self.y = arg

    def to_dictionary(self):
        """Return a dictionary representation of the Rectangle instance."""
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}

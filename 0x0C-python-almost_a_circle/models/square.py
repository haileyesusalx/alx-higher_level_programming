#!/usr/bin/python3
"""module: square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class: Square"""


def __init__(self, size, x=0, y=0, id=None):
    """Method: __init__"""
    super().__init__(size, size, x, y, id)


def __str__(self):
    """Method: __str__"""
    return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                          self.width)


@property
def size(self):
    """Method: size"""
    return self.width


@size.setter
def size(self, value):
    """Method: size"""
    self.width = value
    self.height = value


def update(self, *args, **kwargs):
    """Method: update"""
    if args:
        for i, arg in enumerate(args):
            if i == 0:
                self.id = arg
            elif i == 1:
                self.size = arg
            elif i == 2:
                self.x = arg
            elif i == 3:
                self.y = arg
    else:
        for key, value in kwargs.items():
            if key == 'id':
                self.id = value
            elif key == 'size':
                self.size = value
            elif key == 'x':
                self.x = value
            elif key == 'y':
                self.y = value


def to_dictionary(self):
    """Method: to_dictionary"""
    return {'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y}

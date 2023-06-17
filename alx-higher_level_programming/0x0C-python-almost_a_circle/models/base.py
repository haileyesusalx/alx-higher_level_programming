#!/usr/bin/python3
"""
Module containing the Base class
"""


class Base:
    """
    Base class for the project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the object with an id

        Args:
            id (int): id of the object
        """

        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

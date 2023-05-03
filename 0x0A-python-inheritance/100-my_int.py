#!/usr/bin/python3
"""Module documentation"""


class MyInt(int):
    """Class documentation"""
    def __eq__(self, other):
        """Method documentation"""
        return int(self) != other

    def __ne__(self, other):
        """Method documentation"""
        return int(self) == other

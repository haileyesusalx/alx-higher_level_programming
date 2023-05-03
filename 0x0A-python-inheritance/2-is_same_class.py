#!/usr/bin/python3
"""
This module contains a function that checks if an object
is an instance of a given class.
"""


def is_same_class(obj, a_class):
    """
    Return True if obj is an instance of a_class, otherwise False.
    """
    return type(obj) is a_class

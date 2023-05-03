#!/usr/bin/python3
"""
Module that contains a function to check if an object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that
    inherited (directly or indirectly)
    from the specified class, otherwise False.

    Args:
    - obj: object to check
    - a_class: class to check against

    Return:
    - True if obj is an instance of a subclass of a_class, False otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False

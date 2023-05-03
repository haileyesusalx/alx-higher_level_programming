#!/usr/bin/python3
"""
Module that contains a function to check if an object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited (directly or indirectly)
    from the specified class, otherwise False.

    Args:
    - obj: object to check
    - a_class: class to check against

    Return:
    - True if obj is an instance of a subclass of a_class, False otherwise
    """
    return isinstance(obj, type) and isinstance(a_class, type) and issubclass(obj, a_class) and obj != a_class

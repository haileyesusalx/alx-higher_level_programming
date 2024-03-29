#!/usr/bin/python3
"""a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if obj is an instance of a_class or an instance of a class
    that inherited from a_class, otherwise False.

    Args:
    - obj: object to check
    - a_class: class to check against

    Return:
    - True if obj is an instance of a_class or a subclass of a_class,
    False otherwise
    """
    return isinstance(obj, a_class)

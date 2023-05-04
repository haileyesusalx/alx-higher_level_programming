#!/usr/bin/python3
"""class"""


class Student:
    """define"""

    def __init__(self, first_name, last_name, age):
        """define"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """define"""
        return self

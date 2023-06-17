#!/usr/bin/python3
"""Defines an inherited list class Mylist."""


class MyList(list):
    """Return a  list, but sorted (ascending sort)."""

    def print_sorted(self):
        """print a list in sorted ascending order."""
        print(sorted(self))

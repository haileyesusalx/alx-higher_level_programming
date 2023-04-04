#!/usr/bin/python3
def magic_string():
    magic_str = "BestSchool"
    magic_str += ", " + "BestSchool" * len(magic_str.split(','))
    return magic_str

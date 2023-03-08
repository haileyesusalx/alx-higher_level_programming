#!/usr/bin/python3
def islower(string):
    for char in string:
        if not ('a' <= char <= 'z'):
            return False
    return True


result = islower("z")

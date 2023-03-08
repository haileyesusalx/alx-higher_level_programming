#!/usr/bin/python3
def islower(string):
    for char in string:
        if 'a' <= char <= 'z':
            return True
    return False


result = islower("z")

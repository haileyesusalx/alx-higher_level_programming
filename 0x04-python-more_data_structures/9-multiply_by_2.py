#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v * 2))

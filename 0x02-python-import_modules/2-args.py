#!/usr/bin/python3
def num_of_args(*args):
    a = len(args)
    if a == 1:
        print("{} argument:".format(a))
    else:
        print("{} arguments:".format(a))
    for i, arg in enumerate(args):
        b = i + 1
        print("{}: {}".format(b, arg))



num_of_args()

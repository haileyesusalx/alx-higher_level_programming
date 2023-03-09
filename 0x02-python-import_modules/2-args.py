#!/usr/bin/python3

def num_of_args(*args):
    a = len(args)
    if a == 1:
        print("{} argument:".format(a))
    else:
        print("{} arguments:".format(a))


def num_of_args2(*args):
    for i, arg in enumerate(args):
        b = i + 1
        print("{}: {}".format(b, arg))



if __name__ == "__main__":
    import sys
    num_of_args2(sys.argv[1])
    num_of_args2(sys.argv[2])
    num_of_args2(sys.argv[3])
    num_of_args2(sys.argv[4])
    num_of_args2(sys.argv[5])
    num_of_args2(sys.argv[6])

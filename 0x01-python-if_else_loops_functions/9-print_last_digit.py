#!/usr/bin/python3
def print_last_digit(number):
    b = abs(number) % 10
    print(b, end='')
    return b

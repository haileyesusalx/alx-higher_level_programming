#!/usr/bin/python3
def fizzbuzz():
    number = 5
    Fizz = number % 3
    Buzz = number % 5
    if Fizz == 0:
        print("Fizz")
    elif Buzz == 0:
        print("Buzz")
    elif Fizz == 0 and Buzz == 0:
        print("FizzBuzz")
    else:
        print()

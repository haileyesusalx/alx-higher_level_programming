#!/usr/bin/python3
def fizzbuzz():
    number = range(1, 101)
    for i in number:
        Fizz = i % 3
        Buzz = i % 5
        if Fizz == 0 and Buzz == 0:
            print("FizzBuzz", end=' ')
        elif Fizz == 0 and Buzz != 0:
            print("Fizz", end=' ')
        elif Fizz != 0 and Buzz == 0:
            print("Buzz", end=' ')
        elif Fizz != 0 and Buzz != 0:
            print(i, end=' ')

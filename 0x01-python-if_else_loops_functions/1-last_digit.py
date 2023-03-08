#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
last_digit2 = -1*((-1 * number) % 10)
if number > 0 and last_digit > 5:
    print("Last digit of {} is {} and is greater than 5\n".format(number, last_digit))
elif number > 0 and last_digit == 0:
    print("Last digit of {} is {} and is 0\n".format(number, last_digit))
elif number < 0:
    print("Last digit of {} is {} and is less than 6 and not 0\n".format(number, last_digit2))
else:
    print("Last digit of {} is {} and is less than 6 and not 0\n".format(number, last_digit))

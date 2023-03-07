#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
last_digit2 = -1*((-1 * number) % 10)
if number > 0 and last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif number > 0 and last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
elif number < 0:
    print(f"Last digit of {number} is {last_digit2} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")

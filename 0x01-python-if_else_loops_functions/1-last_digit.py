#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = abs(number) % 10
last_digit2 = int(-1) * int(abs(number) % 10)
if number > 0 and last_digit > 5:
    comparison_string = "and is greater than 5"
    print(f"Last digit of {number} is {last_digit} {comparison_string}")
elif number > 0 and last_digit == 0:
    comparison_string = "and is 0"
    print(f"Last digit of {number} is {last_digit} {comparison_string}")
elif number < 0:
    comparison_string = "and is less than 6 and not 0"
    print(f"Last digit of {number} is {last_digit2} {comparison_string}")
else:
    comparison_string = "and is less than 6 and not 0"
    print(f"Last digit of {number} is {last_digit} {comparison_string}")

#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
sumation = add(10, 5)
result = sub(10, 5)
prod = mul(10, 5)
ques = div(10, 5)
print("{} + {} = {}".format(a, b, sumation))
print("{} - {} = {}".format(a, b, result))
print("{} * {} = {}".format(a, b, prod))
print("{} / {} = {}".format(a, b, ques))

#!/usr/bin/python3
a = range(0, 10)
for i in a:
    for j in a:
        if i != 8 and i < j:
            print(f"{i}{j}", end=', ')
        elif i == 8 and j == 9:
            print(f"{i}{j}", end='')

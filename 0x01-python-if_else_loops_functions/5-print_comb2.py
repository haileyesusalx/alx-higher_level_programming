#!/usr/bin/python3
a = range(0, 100)
for i in a:
    if i < 10:
        print(f"0{i}", end=', ')
    elif i == 99:
        print(i)

    else:
        print(i, end=', ')

#!/usr/bin/python3
alphabet_list1 = range(97, 101)
alphabet_list2 = range(102, 113)
alphabet_list3 = range(114, 123)
a = list(alphabet_list1) + list(alphabet_list2) + list(alphabet_list3)
for characters in list(a):
    b = chr(characters)
    print("{}".format(b), end='')

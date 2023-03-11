#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        my_list = my_list.copy()
        return my_list
    elif idx >= len(my_list):
        my_list = my_list.copy()
        return my_list
    else:
        my_list = my_list.copy()
        my_list[idx] = element
        return my_list

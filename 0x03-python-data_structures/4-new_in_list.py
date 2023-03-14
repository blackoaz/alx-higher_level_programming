#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if my_list[idx] < 0 or my_list[idx] >= len(my_list):
        return new_list
    else:
        my_list[idx] = element

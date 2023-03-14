#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list[idx] < 0 or my_list[idx] >= len(my_list):
        return my_list
    new_list = list(my_list)
    new_list[idx] = element

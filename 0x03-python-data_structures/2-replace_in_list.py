#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for idx in my_list:
        if my_list[idx] < 0 or my_list[idx] >= len(my_list):
            return my_list
        else:
            my_list[idx] = element
            return my_list

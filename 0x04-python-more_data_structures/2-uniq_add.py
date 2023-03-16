#!/usr/bin/python3
def unq_add(my_list=[]):
    if my_list is None:
        my_list = []
    new_list = []
    x = 0
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
            x += i
    return x

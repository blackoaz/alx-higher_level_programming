#!/usr/bin/python3
def unq_add(my_list=[]):
    if my_list is None:
        my_list = []
    new_list = []
    x = 0
    for i in my_list:
        if i in new_list:
            continue
        else:
            new_list.append(i)
            x += i
    print(x)

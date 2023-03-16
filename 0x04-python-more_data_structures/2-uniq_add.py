#!/usr/bin/python3
def unq_add(my_list=[]):
    new_list = []
    x = 0
    for i in my_list:
        if i in new_list:
            continue
        else:
            new_list.append(my_list[i])
            x += my_list[i]
    print(x)            

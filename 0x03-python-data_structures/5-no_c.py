#!/usr/bin/python3
def no_c(my_string):
    string_list = []
    for i in my_string:
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        string_list.append(my_string[i])
        return "".join(string_list)

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len_list = 0
    for item in my_list:
        len_list = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return x
    except IndexError:
        print('The given value for x is out of range')
        return 0
my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))

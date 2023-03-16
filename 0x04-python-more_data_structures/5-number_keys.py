#!/usr/bin/python3
def number_keys(a_dictionary):
    sum = 0
    for k,v in a_dictionary.items():
        sum += k
    print("Number of keys: {:d}".format(sum))

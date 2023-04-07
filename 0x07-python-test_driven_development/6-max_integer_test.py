#!/usr/bin/python3
"""Function for finding the max element in a list
"""


def max_integer(list=[]):
    """Function to finding and returning the max integer in a list
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    output = list[0]
    i = 1
    while i < len(list):
        if list[i] > output:
            output = list[i]
        i += 1
    return output

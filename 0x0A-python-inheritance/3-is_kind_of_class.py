#!/usr/bin/python3
"""Function that check if object is an instance of a class inherited"""


def is_kind_of_class(obj, a_class):
    """checking instance of object and class"""

    if isinstance(obj, a_class):
        return True
    else:
        False

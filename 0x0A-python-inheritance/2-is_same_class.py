#!/usr/bin/python3
"""Function for checking if object is an instance of a class"""


def is_same_class(obj, a_class):
    """checking instance of a class"""

    if isinstance(obj, a_class):
        return True
    else:
        return False

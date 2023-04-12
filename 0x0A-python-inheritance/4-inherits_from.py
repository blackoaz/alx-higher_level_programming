#!/usr/bin/python3
"""function for checking subclass"""


def inherits_from(obj, a_class):
    """checking for subclass"""

    return type(obj) != a_class and issubclass(type(obj), a_class)

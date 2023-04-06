#!/usr/bin/python3
"""Function for adding two integers"""


def add_integer(a, b=98):
    """function for summing up two numbers, the function checks if the values are either integer or float, otherwise raises an error"""

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(a + b)

#!/usr/bin/python3
"""Function for printing square based on #"""


def print_square(size):
    """This function takes the size of a square and produce a square based
    on size
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and isinstance(size < 0):
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")

            print()

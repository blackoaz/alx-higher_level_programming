#!/usr/bin/python3


"""Define a class sqaure"""


class Square:
    """Definition of a class square"""

    def __init__(self, size=0):
        """Initializes a new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """function for calculating the area of the square"""
        area = self.__size * self.__size
        return area

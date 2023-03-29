#!/usr/bin/python3


"""Define a class sqaure"""


class Square:
    """Definition of a class square"""

    def __init__(self, size=0):
        """Initializes a new square

        Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size(self):
        """function for getting the size property"""
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Function for calculating the area of the square"""
        area = self.__size * self.__size
        return area

#!/bin/bash/python3


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

    def area(self):
        """public instance method that returns the current square area"""
        area = self.__size * self.__size
        return area

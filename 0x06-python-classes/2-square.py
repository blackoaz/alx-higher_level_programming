#!/usr/bin/python3
"""defining a square with a default value for size"""


class Square:
    """"class for square"""

    def __init__(self, size=0):
        """Ïnitializing a class"""
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

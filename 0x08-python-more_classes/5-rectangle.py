#!/usr/bin/python3
"""Class for a rectangle"""


class Rectangle:

    """Inside the class for rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation of the variables"""

        self.width = width
        self.height = height

    @property
    def width(self):
        """getter for the width"""

        return self.__width

    @width.setter
    def width(self, value):

        """setter for the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for height"""

        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """function for calculating area"""

        return (self.__height * self.__width)

    def perimeter(self):
        """function for calculating perimeter"""

        if not (self.__height or self.__width):
            return 0
        else:
            return ((2 * self.__height) + (2 * self.__width))

    def __str__(self):
        """string representation for the perimeter and area"""

        if not (self.__width or self.__height):
            return ("")
        hash_print = []
        for i in range(self.__height):
            for j in range(self.__width):
                hash_print.append("#")
            if (i < self.__height - 1):
                hash_print.append("\n")
        return "".join(hash_print)

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

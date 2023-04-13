#!/usr/bin/python3
"""square class that inherits from the class rectangle"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """"square class inheriting from rectangle"""

    def __init__(self, size):
        """initialization for square class"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
            """calculates area method for square, therefore
            overwritting the area method for rectangle
            """
            return self.__size ** 2

#!/usr/bin/python3
"""class for square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class for rectangle"""

    def __init__(self, size: int, x=0, y=0, id=None):
        """constructor for square class"""

        super().__init__(size, size, x, y, id)

        self.__size = size

    def __str__(self):
        """string method"""

        id = self.id
        size = self.__size
        x = self.x
        y = self.y
        return "[square] ({:d}) {:d}/{:d} - {:d}".format(id, x, y, size)

    @property
    def size(self) -> int:
        """"getter for the size"""

        return self.__size

    @size.setter
    def size(self, value: int):
        """setter for the size"""

        self.__size = value
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """method for updating args and kwargs"""

        args_list = ['id', 'size', 'x', 'y']
        if args:
            for pos, loc in zip(args_list, args):
                setattr(self, pos, loc)
        elif kwargs:
            for k, v in kwargs.items():
                if k in args_list:
                    setattr(self, k, v)

    def to_dictionary(self):
        """dictionary method for Square"""

        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

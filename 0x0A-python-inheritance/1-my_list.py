
#!/usr/bin/python3
"""class module MyList that inherits from a list"""


class MyList(list):
    """class inheritting from a class list"""

    def print_sorted(self):
        """function for printing sorted list"n ascending order"""

        sorted_list = sorted(self)
        print(sorted_list)

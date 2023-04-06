#!/usr/bin/python3
"""Function for printing out first name and last name"""


def say_my_name(first_name, last_name=""):
    """This function takes two arguments of first name and last name
    both names should be a string otherwise a type error is raised
    """

    if (not isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if (not isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

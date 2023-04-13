#!/usr/bin/python3
"""function that read text files"""


def read_file(filename=""):
    """function for opening file for reading"""

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")

#!/usr/bin/python3
""" module for searching and updating
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function inserting a line to a text file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        text = ""
        for line in f.readlines():
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as f:
        f.write(text)

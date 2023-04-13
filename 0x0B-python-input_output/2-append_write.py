#!/usr/bin/python3
"""module for appending a text to a file"""


def append_write(filename="", text=""):
    """Function for appending a text to a file"""

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

#!/usr/bin/python3
"""Function that writes string to a textfile
and returns the number of characters written
"""


def write_file(filename="", text=""):
    """fumction for writting into a file"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)

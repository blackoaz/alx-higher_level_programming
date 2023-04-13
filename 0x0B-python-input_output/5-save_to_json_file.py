#!/usr/bin/python3
"""module for writting an object to text file using json"""


import json


def save_to_json_file(my_obj, filename):
    """function for adding object to a file using json"""

    with open(filename, 'w+') as f:
        json.dump(my_obj, f)

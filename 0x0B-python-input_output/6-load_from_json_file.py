#!/usr/bin/python3
"""module that creates an object from a json file"""


import json


def load_from_json_file(filename):
    """function creating an object from json"""

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

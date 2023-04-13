#!/usr/bin/python3
"""Module that returns an object"""


import json


def from_json_string(my_str):
    """function for converting json string
    to objects
    """

    return json.loads(my_str)

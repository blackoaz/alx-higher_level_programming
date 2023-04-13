#!/usr/bin/python3
"""module for returning json representation of a string"""


import json

def to_json_string(my_obj):
    """function for returning json object representation"""

    return json.dumps(my_obj)


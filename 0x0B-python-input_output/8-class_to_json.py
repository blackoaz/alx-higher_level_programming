#!/usr/bin/python3
"""module for returning dictionary with simple data structure"""


def class_to_json(obj):
    """function for creating a dictionary"""

    return obj.__dict__

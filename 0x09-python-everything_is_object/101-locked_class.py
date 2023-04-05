#!/usr/bin/python3
"""This is a LockedClass"""


class LockedClass:
    """Class for preventing users from
        creating new instances
    """
    __slots__ = ["first_name"]

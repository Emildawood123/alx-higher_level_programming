#!/usr/bin/python3
"""moudle"""


class LockedClass:
    """ prevent user to add new attr """
    __slots__ = ["first_name"]

#!/usr/bin/python3
"""class"""


class MyList(list):
    """class"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        return(sorted(self))

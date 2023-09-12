#!/usr/bin/python3
"""module"""


import json


def load_from_json_file(filename):
    """class"""
    with open(filename, "r") as file:
        return (json.loads(file.read()))

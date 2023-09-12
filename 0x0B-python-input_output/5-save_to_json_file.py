#!/usr/bin/python3
"""module"""


import json


def save_to_json_file(my_obj, filename):
    """class"""
    with open(filename, "w") as file:
        return (file.write(json.dumps(my_obj)))

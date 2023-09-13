#!/usr/bin/python3
"""module"""


def append_after(filename="", search_string="", new_string=""):
    """def"""
    with open(filename, "r+") as file:
        my_list = file.readlines()
        file.seek(0)
        for i in my_list:
            file.write(i)
            if (search_string in i):
                file.write(new_string)

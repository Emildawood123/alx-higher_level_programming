#!/usr/bin/python3
"""module"""


def append_after(filename="", search_string="", new_string=""):
    """def"""
    with open(filename, "a") as file:
        num = 0
        my_list = file.readlines()
        for i in my_list:
            num = len(i) + 2
            if (search_string in i):
                file.seek(num)
                file.write(new_string, end="")

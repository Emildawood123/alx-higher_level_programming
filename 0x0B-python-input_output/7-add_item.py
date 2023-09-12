#!/usr/bin/python3
"""module"""


import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """class"""

    my_list = []
    for i in range(1, len(sys.argv)):
        my_list.append(sys.argv[i])
    if not os.path.exists("add_item.json"):
        with open("add_item.json", "w") as file:
            file.write("[]")
    """class"""
    save_to_json_file(my_list, "add_item.json")
    load_from_json_file("add_item.json")


if __name__ == "__main__":
    main()

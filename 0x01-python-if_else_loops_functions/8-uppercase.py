#!/usr/bin/env python3
def uppercase(str):
    string = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            string = string + chr(ord(c) - 32)
        else:
            string = string + c
    print(string)

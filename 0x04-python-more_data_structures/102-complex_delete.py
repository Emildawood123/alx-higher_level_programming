#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    ar = []
    for i in a_dictionary:
        if a_dictionary[i] == value:
            ar.append(i)
    for key in ar:
        a_dictionary.pop(key)
    return (a_dictionary)

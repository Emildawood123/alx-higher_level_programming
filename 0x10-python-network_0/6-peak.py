#!/usr/bin/python3
"""function"""


def find_peak(list_of_integers):
    """function"""
    length = len(list_of_integers)
    list_of_integers = merge_sort(list_of_integers, 0, length - 1)
    return list_of_integers[-1]


def merge_sort(array, start, end):
    """Base case: if there is only one"""
    if end <= start:
        return
    midpoint = (end + start) // 2
    merge_sort(array, start, midpoint)
    merge_sort(array, midpoint + 1, end)

    merge(array, start, midpoint, end)


def merge(array, start, midpoint, end):
    left_length = midpoint - start + 1
    right_length = end - midpoint

    left_array = [0] * left_length
    right_array = [0] * right_length

    for i in range(left_length):
        left_array[i] = array[start + i]

    for j in range(right_length):
        right_array[j] = array[midpoint + 1 + j]
    i = j = 0
    k = start
    while i < left_length and j < right_length:
        if left_array[i] <= right_array[j]:
            array[k] = left_array[i]
            i += 1
        else:
            array[k] = right_array[j]
            j += 1
        k += 1
    while i < left_length:
        array[k] = left_array[i]
        i += 1
        k += 1

    while j < right_length:
        array[k] = right_array[j]
        j += 1
        k += 1

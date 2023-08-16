#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    res = 0
    for i in my_list:
        if i in new:
            continue
        else:
            new.append(i)
    for j in new:
        res = res + j
    return (res)


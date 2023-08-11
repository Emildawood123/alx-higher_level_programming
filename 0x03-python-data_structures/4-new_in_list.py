#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = []
    count = 0
    if idx < 0 or idx > len(my_list) + 1:
        return (my_list)
    else:
        for i in my_list:
            if count == idx:
                new.append(element)
                count += 1
            else:
                new.append(i)
                count += 1
        return (new)

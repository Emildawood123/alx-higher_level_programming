#!/usr/bin/python3
def best_score(a_dictionary):
    best = ""
    score = 0
    if a_dictionary is None:
        return None
    else:
        for i in a_dictionary:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                best = i
            else:
                continue
    return best

#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0
    if (type(roman_string) != str or roman_string is None):
        return 0
    else:
        last = roman_dic[roman_string[len(roman_string) - 1]]
        res += last
        for i in range(len(roman_string) - 1):
            if roman_dic[roman_string[i]] >= last:
                res += roman_dic[roman_string[i]]
            else:
                res -= roman_dic[roman_string[i]]
    return res

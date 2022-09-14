#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {
            'I': 1,
            "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    if not isinstance(roman_string, str) or roman_string is None:
        return (0)
    length = len(roman_string)

    for i in range(length):
        if i == (length - 1):
            res = res + roman_dict[roman_string[i]]
        else:
            if roman_dict[roman_string[i]] >= roman_dict[roman_string[i + 1]]:
                res = res + roman_dict[roman_string[i]]
            else:
                res = res - roman_dict[roman_string[i]]
    return (res)

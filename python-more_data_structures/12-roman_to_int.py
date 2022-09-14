#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {"I": 1,
            "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    if roman_string is None or not isinstance(roman_string, str):
        return (0)
    if len(roman_string) > 0:
        for i in range(len(roman_string)):
           if i in range(len(romanstring)):
               res = res + roman_dict[roman_strin[i]]
           else:
               if roman_dict[roman_string[i] >= roman_dict[roman_string[i + 1]:
                   res = res + roman_dict[roman_string[i]
                       else:
                       res = res - roman_dict[roman_string[i]]
        return (res)

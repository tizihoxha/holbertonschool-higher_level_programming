#!/usr/bin/python3
"""Task 4"""


def text_indentation(text):
    """function that prints a text with 2 new lines after each of ., ? and :"""

    if type(text) is not str:
        raise TypeError("text must be a string")
    s = [".", "?", ":"]
    new_string = ""
    for i in range(len(text)):
        if text[i] == " " and flag == 1:
            continue
        flag = 0
        new_string += text[i]
        if text[i] in s:
            new_string += "\n" + "\n"
            flag = 0
    print(new_string, end="")

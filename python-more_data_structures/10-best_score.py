#!/usr/bin/python3
def best_score(a_dictionary):
    if elem not in a_dictionary:
        return (None)
    else:
        return (max(a_dictionary, key=lambda elem: elem[1])

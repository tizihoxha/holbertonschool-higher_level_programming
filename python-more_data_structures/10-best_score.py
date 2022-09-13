#!/usr/bin/python3
def best_score(a_dictionary):
    if elem in a_dictionary:
        return (max(a_dictionary.elem(), key=operator.itemgetter(1))[0])
    if elem not in a_dictionary:
        return (None)

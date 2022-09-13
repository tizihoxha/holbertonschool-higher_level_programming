#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for search, elem in enumerate(my_list):
        return [replace if search == elem else elem]

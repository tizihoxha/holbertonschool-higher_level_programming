#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return (my_list)
    else:
        reversed_list = my_list[::-1]
    for i in range(len(reversed_list)):
        print("{:d}".format(reversed_list[i]))

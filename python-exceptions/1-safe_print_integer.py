#!/usr/bin/python3
def safe_print_integer(value):
    i = 0
    for num in range(0,x):
        try:
            print("{:d}".format(my_list[i]), end="")
            i = i + 1
        except (ValueError, TypeError):
            continue
    print("")
    return (i)

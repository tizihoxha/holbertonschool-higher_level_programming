#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 1
    total = 0
    while i != (len(argv)):
        total = total + int(argv[i])
        i = i + 1
    print("{}".format(total))

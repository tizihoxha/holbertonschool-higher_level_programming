#!/usr/bin/python3
def read_text():
    with open("file1.txt") as f:
        [print(line) for line in f.readlines()]

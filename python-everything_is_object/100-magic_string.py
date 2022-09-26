#!/usr/bin/python3
def magic_string(l=[0]):
    l[0] = l[0] + 1
    return (", ".join(["Holberton" for i in range(l[0])]))

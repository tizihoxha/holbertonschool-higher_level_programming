#!/usr/bin/python3
"""Task 1"""


def matrix_divided(matrix, div):
    """function that divides all elements of a matrix"""

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len({len(list) for list in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for num in row:
            if not num or type(num) is not int and type(num) is not float:
                raise TypeError("matrix must be a matrix (list of lists)" + 
                        "of integers/floats")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])



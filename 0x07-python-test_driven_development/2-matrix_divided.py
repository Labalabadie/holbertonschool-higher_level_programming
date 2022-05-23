#!/usr/bin/python3
def matrix_divided(matrix, div):

    row_len = []
    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row_len.append(len(row))

        if not all(elem == row_len[0] for elem in row_len):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    return new_matrix

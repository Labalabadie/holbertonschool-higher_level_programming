#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for i, line in enumerate(matrix):
        new_matrix[i] = list(map(pow, line))
    return new_matrix


def pow(x):
    return x * x

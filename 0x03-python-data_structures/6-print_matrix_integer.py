#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("")
    for line in matrix:
        print('  '.join(map(str, line)))

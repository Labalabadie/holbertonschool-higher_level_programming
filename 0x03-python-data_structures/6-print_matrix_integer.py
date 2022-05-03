#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i, elem in enumerate(line):
            print(f"{elem}", end="")
            if len(line) - 1 != i:
                print(" ", end="")
        print()

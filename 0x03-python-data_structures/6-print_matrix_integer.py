#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for m in matrix:
        for i in m:
            print("{:3d}".format(i), end="")
        print()

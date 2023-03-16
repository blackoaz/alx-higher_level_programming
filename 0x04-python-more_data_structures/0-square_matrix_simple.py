#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for row in matrix:
        for element in row:
            print(element ** 2, end=" " if element != row[-1] else "")
        print()

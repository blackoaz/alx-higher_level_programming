#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix
    for row in new_matrix:
        for element in row:
            print(element ** 2, end=" " if element != row[-1] else "")
        print()

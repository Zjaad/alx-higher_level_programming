#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    amatrix = []
    for x in matrix:
        y = []
        for i in x:
            y.append(i ** 2)
        amatrix.append(y)
    return amatrix

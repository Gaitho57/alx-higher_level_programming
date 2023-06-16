#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for in_dex in range(len(matrix)):
        new_matrix[in_dex] = list(map(lambda x: x**2, matrix[in_dex]))

    return (new_matrix)

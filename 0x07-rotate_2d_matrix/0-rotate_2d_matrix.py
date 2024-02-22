#!/usr/bin/python3

"""
Rotate 2D Matrix module
"""


def rotate_2d_matrix(matrix):
    """
    rotate n x n 2D matrix
    """
    if type(matrix) is not list or len(matrix) <= 0:
        return
    n = len(matrix)
    matrix_copied = matrix.copy()
    matrix.clear()

    # Rotate the matrix by 90 degrees
    for col in range(n):
        temp_row = [matrix_copied[row][col] for row in range(n - 1, -1, -1)]
        matrix.append(temp_row)

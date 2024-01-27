#!/usr/bin/python3


"""
Pascal triangle module.
"""


def pascal_triangle(n):
    """Implement the pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = []
    pascal_triangle.append([1])
    for _ in range(1, n):
        if len(pascal_triangle) > 0:
            row = [1]
            for num in range(1, len(pascal_triangle[-1])):
                row.append(pascal_triangle[-1][num] +
                           pascal_triangle[-1][num - 1])
            row.append(1)
            pascal_triangle.append(row)
    return (pascal_triangle)

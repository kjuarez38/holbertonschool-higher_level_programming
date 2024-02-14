#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """pascal triangle"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [None for _ in range(i + 1)]
        row[0], row[-1] = 1, 1

        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)

    return triangle

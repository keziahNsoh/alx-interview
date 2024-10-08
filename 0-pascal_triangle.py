#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """Returns a list of lists representing Pascal's triangle of n."""
    if n <= 0:
        return []

    triangle = []  # This will hold the rows of Pascal's Triangle

    for row_num in range(n):
        row = [1] * (row_num + 1)  # Initialize a row with 1s

        # Calculate the values for the inner elements of the row
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

        triangle.append(row)  # Add the row to the triangle

    return triangle

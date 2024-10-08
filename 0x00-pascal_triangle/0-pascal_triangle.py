#!/usr/bin/python3
"""
pascal's triangle
"""


def pascal_triangle(n):
    """This is a function for making pascal's triangle in a form of lists
    Args:
        - n: the number of rows in the triangle
    Returns:
        - list of lists in case of n > 0
        - empty list in case of n <= 0
    """
    pascal = []
    if n <= 0:
        return pascal
    for i in range(n):
        pre = [(1 if j == 0 or j == i else
                pascal[i - 1][j] + pascal[i - 1][j - 1])
               for j in range(i + 1)]
        pascal.append(pre)

    return pascal

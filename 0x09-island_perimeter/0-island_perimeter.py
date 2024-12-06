#!/usr/bin/python3
"""
Module to calculate the perimeter of an island described in a grid.
"""


def island_perimeter(grid):
    """
    Function that returns the perimeter of the island described in grid.

    Args:
    grid (list of list of integers): 2D grid where 1 is land and 0 is water.

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # If it's land
                # Check the four directions (up, down, left, right)
                if i == 0 or grid[i - 1][j] == 0:  # Top
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Bottom
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Right
                    perimeter += 1

    return perimeter

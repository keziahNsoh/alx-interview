#!/usr/bin/python3
"""
Module for determining if all boxes can be opened.

The function canUnlockAll takes a list of boxes, where each box contains
keys to other boxes. The first box is initially unlocked.

Returns True if all boxes can be opened, otherwise returns False.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
        boxes (list of list of int): The list of boxes with their keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # The first box is unlocked
    stack = [0]  # Start with the first box

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and not visited[key]:  # Check if the key is valid
                visited[key] = True  # Mark the box as visited
                stack.append(key)  # Add it to the stack to explore later

    return all(visited)

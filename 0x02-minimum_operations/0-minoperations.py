#!/usr/bin/python3
"""Module to calculate minimum operations to achieve n characters."""


def minOperations(n):
    """Calculate the fewest number of operations
    to reach exactly n characters."""
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    # Factor n and count operations based on prime factors
    while n > 1:
        if n % factor == 0:
            operations += factor  # We need `factor` operations
            n //= factor  # Reduce n by the factor
        else:
            factor += 1  # Move to the next possible factor

    return operations

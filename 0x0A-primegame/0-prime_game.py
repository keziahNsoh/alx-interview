#!/usr/bin/python3
"""Module for determining the winner of the Prime Game."""


def isWinner(x, nums):
    """
    Determine who wins the most rounds of the prime game.

    Args:
        x (int): The number of rounds to play
        nums (list): An array of n for each round

    Returns:
        str: Name of the player that won the most rounds (Maria/Ben)
        None: If the winner cannot be determined
    """
    if not isinstance(x, int) or x < 1 or not nums:
        return None
    if x != len(nums):
        return None
    if x > 10000 or any(n > 10000 for n in nums):
        return None

    maria_wins = ben_wins = 0

    def get_primes_up_to(n):
        """Return list of primes from 2 to n using Sieve of Eratosthenes."""
        if n < 2:
            return []
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, n + 1, i):
                    sieve[j] = False

        return [i for i, is_prime in enumerate(sieve) if is_prime]

    for n in nums:
        primes = get_primes_up_to(n)
        if not primes:
            ben_wins += 1
        elif len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None

#!/usr/bin/python3


def sieve_of_eratosthenes(n):
    """Return all prime numbers up to n using the Sieve of Eratosthenes."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not primes

    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i in range(2, n + 1) if sieve[i]]


def play_game(n):
    """Simulate a game for a given value of n and return the winner."""
    primes = sieve_of_eratosthenes(n)
    primes_set = set(primes)
    turn = 0  # Maria starts, 0 is Maria's turn, 1 is Ben's turn

    while primes_set:
        # Maria or Ben pick the smallest prime
        prime_to_remove = min(primes_set)
        primes_set.remove(prime_to_remove)

        # Remove the multiples of the chosen prime
        multiples = set(range(prime_to_remove * 2, n + 1, prime_to_remove))
        primes_set -= multiples

        # Switch turn: 0 becomes 1, and 1 becomes 0
        turn = 1 - turn

    # If turn is 0 after the loop,Ben made the last move, so Maria won
    return "Ben" if turn == 0 else "Maria"


def isWinner(x, nums):
    """Return the player who won the most rounds or None if there's a tie."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

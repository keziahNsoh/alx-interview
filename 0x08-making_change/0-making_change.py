#!/usr/bin/python3


def make_change(coins, total):
    """
    Determines the fewest number of coins needed to make a given total.

    Args:
        coins (list): List of coin denominations available.
        total (int): The target amount to make with the coins.

    Returns:
        int: The minimum number of coins needed to make the total.
             Returns -1 if the total cannot be made with the given coins.
    """
    if total <= 0:
        return 0

    # Initialize the DP array, with a value greater than total (infinity)
    inf = float("inf")
    dp = [inf] * (total + 1)

    # Base case: 0 coins needed to make 0
    dp[0] = 0

    # Loop through each coin and update the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If total is still infinity,it means it's not possible to make that total
    return dp[total] if dp[total] != inf else -1

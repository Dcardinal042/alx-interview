#!/usr/bin/python3
"""
Module for making change problem
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): List of coin values.
        total (int): Target total.

    Returns:
        int: Fewest number of coins needed to meet the total.
              If total is 0 or less, returns 0.
              If total cannot be met by any number of coins, returns -1.
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


# Uncomment the following lines to test the provided examples
# print(makeChange([1, 2, 25], 37))  # Output: 7
# print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1


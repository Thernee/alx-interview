#!/usr/bin/python3

"""
Coin change problem module
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0
    # coins = [coin for coin in coins if coin <= total]

    coins.sort(reverse=True)
    number_of_coins = 0
    for coin in coins:
        holder = total // coin
        if holder > 0:
            number_of_coins += holder
            total = total % coin
    if total > 0:
        return -1
    return number_of_coins

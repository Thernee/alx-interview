#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determine the winner of a Prime Game
    """
    if x is None or nums is None or x == 0:
        return None
    # primes_list = sieve_of_Eratosthenes(max(nums))
    # temp = [primes % 2 == 0 for primes in primes_list]

    temp = [True for num in nums if len(sieve_of_Eratosthenes(num)) % 2 == 0]
    ben = sum(temp)
    maria = len(nums) - ben

    if ben == maria:
        return None
    elif ben < maria:
        return "Maria"
    else:
        return "Ben"


def sieve_of_Eratosthenes(n):
    """
    Return primes between 1 and n (inclusive)
    """
    # if n < 2:
    #     return []
    # primes = [True for i in range(n + 1)]
    # primes[0] = primes[1] = False
    # for i in range(2, int(n ** 0.5) + 1):
    #     if primes[i]:
    #         for j in range(i * i, n + 1, i):
    #             primes[j] = False
    # return [i for i in range(n + 1) if primes[i]]
    primes = []
    filter = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filter[prime]):
            primes.append(prime)
            for i in range(prime, n + 1, prime):
                filter[i] = False
    return primes

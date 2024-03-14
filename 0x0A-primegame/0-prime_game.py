#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    """
    Determine winner of prime game
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    ben, maria = 0, 0
    primes = filter_primes(nums)

    for num in range(x):
        if primes[num] % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben == maria:
        return None
    elif ben > maria:
        return 'Ben'
    return 'Maria'


def filter_primes(arr):
    """
    Filter primes
    """
    primes = []
    for num in arr:
        if is_prime(num):
            primes.append(num)
        else:
            primes.append(0)
    return primes


def is_prime(num):
    """
    Check if number is prime
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        return True

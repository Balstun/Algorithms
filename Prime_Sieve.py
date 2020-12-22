# Objective: Build an array of prime numbers in the range n as an array

import math as mt


def is_prime(num):
    if num < 2:  # Checks if number is negative, 0, or 1
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:  # Checks if number is divisible by 2 or 3, most common prime factors
        return False
    sqrt_n = int(mt.sqrt(num)) + 1
    for i in range(6, sqrt_n + 1, 6):
        # Tests divisibility against all numbers that are mod 6 equivalent with a remainder of 1 or 5.
        # All of these numbers aren't divisible by 2 or 3
        if num % (i - 1) == 0 or num % (i + 1) == 0:
            return False
    return True


is_prime.__doc__ = 'Evaluates a number to be prime. Returns true if prime, false otherwise.'


def prime_sieve(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


prime_sieve.__doc__ = 'Builds an array of prime numbers less than or equal to n'


n = int(input())
primes = prime_sieve(n)

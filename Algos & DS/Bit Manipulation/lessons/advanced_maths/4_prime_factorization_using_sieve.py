'''
You are given a positive number N. Using the concept of Sieve, compute its prime factorisation.
'''

from typing import List


class Solution:
  def __init__(self):
    # Initialize the sieve limit to a small value
    self.sieve_limit = 10**6  # Adjust based on expected input size
    self.primes = self.sieve()

  def sieve(self):
    """Generate all prime numbers up to the sieve limit using the Sieve of Eratosthenes."""
    sieve = [True] * (self.sieve_limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for num in range(2, int(self.sieve_limit**0.5) + 1):
      if sieve[num]:
        # Mark multiples of num as non-prime
        sieve[num*num : self.sieve_limit+1 : num] = [False] * len(sieve[num*num : self.sieve_limit+1 : num])

    # Collect all prime numbers
    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    return primes

  def findPrimeFactors(self, N):
    """Find the prime factors of N using the precomputed list of primes."""
    if N < 2:
      return []  # No prime factors for numbers less than 2

    factors = []
    for prime in self.primes:
      if prime * prime > N:
        break  # No need to check further if prime^2 > N
      while N % prime == 0:
        factors.append(prime)
        N //= prime
      if N == 1:
        break

    if N > 1:
      factors.append(N)  # N itself is a prime number

    return factors

N = 12246
# Output: 2 3 13 157
# Explanation: 2*3*13*157 = 12246 = N.
'''
Given an integer n, return the number of prime numbers that are strictly less than n.
'''

class Solution:
  def countPrimes(self, n: int) -> int:
    # Step 1: Initialize a boolean list to track prime numbers (0 to n)
    # All entries start as True, except indices 0 and 1 (non-primes)
    isPrime = [True] * (n+1)
    isPrime[0] = isPrime[1] = False  # 0 and 1 are not primes
    
    # Step 2: Iterate over potential primes from 2 up to sqrt(n)
    # If n is not prime, it must have a factor ≤ sqrt(n)
    for p in range(2, int(n**0.5)+1):
      if isPrime[p]: # p is confirmed as a prime
        # Mark all multiples of p starting from p^2 as non-prime
        # Smaller multiples (e.g., p*2, p*3) are already marked by earlier primes
        for multiple in range(p*p, n+1, p):
          isPrime[multiple] = False
          
    # Step 3: Collect all indices that remain marked as True (primes)
    return [i for i, prime in enumerate(isPrime) if prime]


'''
Why check up to sqrt(n) inclusive?

# To check if a number `n` has prime factors, testing up to `sqrt(n)` is sufficient.  
# If `n` has a factor `a > sqrt(n)`, the corresponding factor `b = n/a` must be `<= sqrt(n)`.  
# If no factors `<= sqrt(n)` exist, `n` cannot be composite (its smaller factor would already have been found).  
# This reduces the search space, optimizing primality checks and sieve-based algorithms like Sieve of Eratosthenes.

11^(1/2) = 3.31
4*4 = 16 > 11
3.5*3.5 = 12.25 > 11
'''
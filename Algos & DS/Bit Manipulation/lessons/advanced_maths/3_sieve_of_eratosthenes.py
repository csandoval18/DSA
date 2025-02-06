class Solution:
  def countPrimes(self, n: int) -> int:
    if n <= 2:
      return 0
    
    primes = [True]*n
    primes[0] = primes[1] = False # Mark 0 and 1 as non prime numbers
    
    for i in range(2, int(n**0.5)+1): # divisors can not exceed sqrt(N)
      if primes[i]:
        primes[i*i:n:i] = [False] * len(range(i*i, n, i))
    return sum(primes)
    
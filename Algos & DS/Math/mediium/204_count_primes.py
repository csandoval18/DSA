"Given an integer n, return the number of prime numbers that are strictly less than n."

class Solution:
  def countPrimes(self, n: int) -> int:
    if n <= 2:
      return 0
    
    # Intialize a boolean array to track prime numbers
    isPrime = [True]*n
    isPrime[0] = isPrime[1] = False # 0 and 1 are not primes
    
    # Iterate from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
      if isPrime[i]:
        # Mark multiples of i as not prime
        isPrime[i*i:n:i] = [False] * len(range(i*i, n, i))
    return sum(isPrime)
    
# n^a * n^b = n^(a+b)
# (n^a)^b = n^(a*b)

# (n^(1/2))^2 = n^((1/2)*2) = n^1 = n
# n^(a/b) = (b sqrt(n))^a

# Square root: n^(1/2) = √n
# Cube root: n^(1/3) = 3√n
# Fourth root: n^(1/4) = 4√n
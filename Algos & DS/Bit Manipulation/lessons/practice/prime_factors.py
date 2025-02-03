from typing import Tuple


# class Solution:
#   def AllPrimeFactors(self, N: int) -> Tuple[int, int]:
#     factors = set() # To stor eunique prime factors
#     divisor = 2 # Start with the smallest prime numbers
    
#     # Handle factors of 2 separately
#     while N % divisor == 0:
#       factors.add(divisor)
#       N //= divisor
    

'''
Explanation:
Numbers less than or equal to 1: These are not prime by definition.

2 and 3: These are prime numbers.

Multiples of 2 and 3: If the number is divisible by 2 or 3, it's not prime.

Check factors from 5 to the square root of n: We only need to check divisibility up to the square
root of n because if n has a factor greater than its square root, the corresponding factor must be less than the square root. We increment by 6 because we've already eliminated multiples of 2 and 3.
''' 

class Solution:
  def AllPrimeFactors(self, N: int) -> Tuple[int, int]:
    res = []
    
    for i in range(2, n+1):
      if n%1 == 0:
        if self.isPrime(i):
          res.append(i)   
      
  
  def isPrime(n):
    # Numbers less than or equal to 1 are not prime
    if n <= 1:
      return False
    # 2 and 3 are prime numbers
    if n <= 3:
      return True
    # Eliminate multiples of 2 and 3
    if n % 2 == 0 or n % 3 == 0:
      return False
    # Check for factors from 5 to the square root of n
    i = 5
    while i * i <= n:
      if n % i == 0 or n % (i+2) == 0:
        return False
      i += 6
    return True
    
class Solution:
  def AllPrimeFactors(self, N: int) -> Tuple[int, int]:
    
    
n = 60

# 1,2,3,4,5,6,10
# 12,18,20,30,60


n = 100
# Output: 2 5
# Explanation: 2 and 5 are the unique prime factors of 100.
s = Solution()

'''
50. Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (ie. x^n)
'''

class Solution:
  def myPow(self, x: float, n: int) -> float:
    def helper(x: int, n: int) -> int:
      if n == 0:
        return 1
      if n == 1:
        return x
      
      half = helper(x , n//2)
      if n % 2 == 0:
        return half * half
      else:
        return half * half * x
    
    if n < 0:
      x = 1 / x
      n = -n
    return helper(x, n)
      
"""
Approach:
1. Recursive Approach with Divide and Conquer:
  - The idea is to use the property that x^n = x^(n/2) * x^(n/2) if n is even.
  - If n is odd, we can write x^n = x * x^(n-1).
  - This approach reduces the problem size by half at each step, leading to a time complexity of O(log n).

2. Handling Negative Exponents:
  - If n is negative, we can convert the problem to calculating (1/x)^(-n).

3. Base Cases:
- If n == 0, the result is 1.
- If n == 1, the result is x.
"""

x = 2.00000
n = 10
# Output: 1024.00000

x = 2.10000
n = 3
# Output: 9.26100

x = 2.00000
n = -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
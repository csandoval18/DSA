'''
Given an integer n, break it into the sum of k positive integers,
where k >= 2, and maximize the product of those integers.

Return the maximum product you can get
'''

class SolutionSimple:
  def integerBreak(self, n: int) -> int:
    # Base cases
    if n == 2:
      return 1
    if n == 3:
      return 2
    
    product = 1
    # Divide by 3 as much as possible
    while n > 4:
      product *= 3
      n -= 3
    
    # Multiply the remainder to the product
    product *= n
    return product


class SolutionRec: 
  def integerBreak(self, n: int) -> int:
    def helper(x: int):
      # Base case: When x reaches 1 we stop breaking down further since 1 can't be split, and the recursion terminates.
      if x == 1:
        return 1
      
      # Initialize the max produt for curr x
      max_prod = 0
      # Try splitting x into two parts: i and x-i
      for i in range(1, x):
        # Product of i and the max obtainable from breaking (x-i)
        max_prod = max(max_prod, i * max(x-i, helper(x-i)))
      return max_prod
    return helper(n)


class SolutionMemo:
  def integerBreak(self, n: int) -> int:
    def helper(x: int) -> int:
      if x == 1:
        return 1
      
      if dp[x] != -1:
        return dp[x]
      
      # Initialize the max product for current x
      max_prod = 0
      # Try splitting x into two parts: i and x-i
      for i in range(1, x):
        # Product of i and the max obtainable from breaking (x-i)
        max_prod = max(max_prod, i * max(x-i, helper(x-i)))
        
      dp[x] = max_prod
      return dp[x]
    
    dp = [-1]*(n+1)
    return helper(n)


class SolutionMemo:
  def integerBreak(self, n: int) -> int:
    # Edge case for small values of n
    if n == 2:
      return 1 
    if n == 3:
      return 2
    
    # Initialize the dp array with base cases
    dp = [0] * (n+1)
    dp[1] = 1
    
    # Fill the dp array from 2 to n
    for i in range(2, n+1):
      maxProd = 0
      # Check all possible splits
      for j in range(1, i):
        # Take the max of breaking or not breaking the second part
        maxProd = max(maxProd, j * (i-j), j * dp[i-j])
      dp[i] = maxProd
    return dp[n]
    
    
    
n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 * 1 = 1

n = 10
# Output: 36
# Explnation: 10 = 3 + 3 + 4, 3 * 3 * 4 = 36
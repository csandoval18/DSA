'''
Given a positive integer n, you can apply one of the following operations:
1. If n is even, replace n with n / 2.
2. If n is odd, replace n with either n + 1 or n - 1.

Return the minimum number of operations needed for n to become 1.
'''

class SolutionRec:
  def integerReplacement(self, n: int) -> int:
    def helper(n: int) -> int:
      if n <= 1:
        return 0
        
      op = 0
      if n % 2 == 0:
        op += 1 + helper(n // 2)
      else:
        op += 1 + min(helper(n-1), helper(n+1))
        
      return op
    return helper(n)
      

class SolutionMemo:
  def integerReplacement(self, n: int) -> int:
    memo = {}
    def helper(x: int) -> int:
      if x == 1:
        return 0
      
      if x in memo:
        return memo[x]
        
      op = 0
      if x % 2 == 0:
        op += helper(x // 2)
      else:
        op += min(helper(x-1), helper(x+1))
        
      return op
    return helper(n)


class SolutionDP:
  def integerReplacement(self, n: int) -> int:
    dp = [0] * (n+2)
    # dp[1] = 0
    
    for x in range(n):
      if x%2 == 0:
        dp[x] = 1 + dp[x // 2]
      else:
        dp[x] = 1 + min(dp[x-1, dp[x+1]])
    return dp[n]
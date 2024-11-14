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
      

class SolutionMemo: # Answer accepted
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


class SolutionMemo2:
  def integerReplacement(self, n: int) -> int:
    memo = {}

    def helper(x: int) -> int:
      if x == 1:
        return 0
      if x in memo:
        return memo[x]
      
      if x % 2 == 0:
        # If x is even, just divide by 2
        result = 1 + helper(x // 2)
      else:
        # If x is odd, we have two paths:
        # 1. Subtract 1 to make it even (helper(x - 1))
        # 2. Add 1 to make it even and then divide by 2 (helper((x + 1) // 2) + 1)
        result = 1 + min(helper(x - 1), helper((x + 1) // 2) + 1)
          
      memo[x] = result
      return result
    
    return helper(n)


class SolutionDP: # Memory limited exceeded
  def integerReplacement(self, n: int) -> int:
    dp = [0] * (n+1)
    dp[1] = 0 # Base case: 1 needs 0 replacements to become 1
    
    for x in range(2, n+1):
      if x%2 == 0:
        dp[x] = 1 + dp[x // 2]
      else:
        dp[x] = 1 + min(dp[x-1, dp[(x+1)//2] + 1])
    return dp[n]
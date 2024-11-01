class SolutionAttempt:
  def guessNumber(self, n: int) -> int:
    def helper(left: int, right: int):
      if left >= right:
        return 0
      
      m = (left + right) // 2
      higher = m + helper(m+1, right)
      lower = m + helper(left, m-1)
      return max(higher, lower)
    return helper(1, n)


class SolutionRec:
  def guessNumber(self, n: int) -> int:
    def helper(left: int, right: int) -> int:
      # Base case: no cost needed if the range has no numbers
      if left >= right:
        return 0
      
      min_cost = float('inf')
      for m in range(left, right+1): # Try every possible guess in the range [left, right]
        cost = m + max(helper(left, m-1), helper(m+1, right)) # Cost of the guess m
        min_cost = min(min_cost, cost) # Update the min cost
      return min_cost
    return helper(1, n)
  

class SolutionMemo:
  def getMoneyAmount(self, n: int) -> int:
    def helper(left: int, right: int) -> int:
      if left >= right:
        return 0
      
      if dp[left][right] != -1:
        return dp[left][right]
      
      min_cost = float('inf')
      for x in range(left, right+1):
        cost = x + max(helper(left, x-1), helper(x+1, right))
        min_cost = min(min_cost, cost)
      dp[left][right] = min_cost
      return dp[left][right]
    
    dp = [[-1] * (n+1) for _ in range(n+1)]
    return helper(1, n)


class SolutionDP:
  def getMoneyAmount(self, n: int) -> int:
    dp = [[0] * (n+1) for _ in range(n+1)]
    
    # Outer loop: iterate over lengths of the ranges
    for length in range(2, n+1):  # Start with 2 because length 1 has no cost
      # Middle loop: start of the range
      for left in range(1, n - length + 2):
        right = left + length - 1
        dp[left][right] = float('inf')
        
        # Inner loop: guess each number x within the range [left, right]
        for x in range(left, right+1):
          # Bound check for subproblems
          cost = x + max(dp[left][x-1] if x -1 >= left else 0, dp[x+1][right] if x + 1 <= right else 0)
          dp[left][right] = min(dp[left][right], cost)
    # The answer for the full range [1, n] is dp[1][n]
    return dp[1][n]
from typing import List

# Recursive
def minPathSumRec(matrix: List[List[int]]) -> int:
  def helper(i: int, j: int) -> int:
    if i == 0 and j == 0:
      return matrix[0][0]
    
    if i < 0 or j < 0:
      return float('inf')
    
    up = helper(i-1, j)
    down = helper(i, j-1)
    
    return min(up, down)

# If overlapping subproblems present in recursion tree => Memoization
def minPathSumMemo(matrix: List[List[int]]) -> int:
  def helper(i: int, j: int, dp: List[List[int]]) -> int:
    if i == 0 and j == 0:
      return matrix[0][0]
    
    if i < 0 or j < 0:
      return float('inf')
      
    if dp[i][j] != -1:
      return dp[i][j]
    
    up = helper(i-1, j)
    left = helper(i, j-1)
    
    dp[i][j] = min(up, left)
    return dp[i][j]
  
  dp = [[-1 for _ in range(m)] for _ in range(n)]
  n = len(matrix)
  m = len(matrix[0])
  return helper(n-1, m-1, dp)

# Tabulation 
def minPathSum(matrix: List[List[int]]) -> int:
  n = len(matrix)
  m = len(matrix)
  dp = [[-1 for _ in range(m)] for _ in range(n)]
  
  for i in range(n):
    for j in range(m):
      if i == 0 and j == 0:
        dp[i][j] = matrix[i][j]
      else:
        up = matrix[i][j]
        if i > 0:
          up += dp[i-1][j]
        else:
          up += int(1e9)
        
        left = matrix[i][j]
        if j > 0:
          left += matrix[i][j]
        else:
          # We have reached the farthest left index, set the left to a big integer
          left += int(1e9)
          
        dp[i][j] = min(up, left)
      
  return dp[n-1][m-1]
        
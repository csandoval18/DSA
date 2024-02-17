from typing import List

# Recursive
def minPathSumRec(matrix: List[List[int]]) -> int:
  def helper(i: int, j: int) -> int:
    if i == 0 and j == 0:
      return matrix[0][0]
    
    if i < 0 or j < 0:
      return int(1e9)
    
    up = matrix[i][j] + helper(i-1, j)
    left = matrix[i][j] + helper(i, j-1)
    
    return min(up, left)
  
  n = len(matrix)
  m = len(matrix[0])
  res = int(1e9)
  return helper(n-1, m-1)

# If overlapping subproblems present in recursion tree => Memoization
def minPathSumMemo(matrix: List[List[int]]) -> int:
  def helper(i: int, j: int, dp: List[List[int]]) -> int:
    if i == 0 and j == 0:
      return matrix[0][0]
    
    if i < 0 or j < 0:
      return int(1e9)
      
    if dp[i][j] != -1:
      return dp[i][j]
    
    up = matrix[i][j] + helper(i-1, j, dp)
    left = matrix[i][j] + helper(i, j-1, dp)
    
    dp[i][j] = min(up, left)
    return dp[i][j]
  
  n = len(matrix)
  m = len(matrix[0])
  dp = [[-1 for _ in range(m)] for _ in range(n)]
  return helper(n-1, m-1, dp)

# Tabulation 
def minPathSumTab(matrix: List[List[int]]) -> int:
  n = len(matrix)
  m = len(matrix[0])
  dp = [[0 for _ in range(m)] for _ in range(n)]
  
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
          left += dp[i][j-1]
        else:
          # We have reached the farthest left index, set the left to a big integer
          left += int(1e9)
          
        dp[i][j] = min(up, left)
      
  return dp[n-1][m-1]
        
# Space Optimization
def minPathSumSO(matrix: List[List[int]]) -> int:
  n = len(matrix)
  m = len(matrix[0])
  # dp = [[-1 for _ in range(m)] for _ in range(n)]
  
  prevRow = matrix[0]
  for i in range(n):
    currRow = [0] * m 
    
    for j in range(m):
      if i == 0 and j == 0:
        currRow[j] = matrix[i][j]
      else:
        up = matrix[i][j]
        if i > 0:
          up += prevRow[j]
        else:
          # We have surpassed the farthest top index, set the up val to a big integer
          # so it loses the min comparison
          up += int(1e9)
        
        left = matrix[i][j]
        if j > 0:
          left += currRow[j-1]
        else:
          # We have surpassd the farthest left index, set the left val to a big integer
          # so it loses the min comparison
          left += int(1e9)
          
        currRow[j] = min(up, left)
    
    prevRow = currRow
      
  return prevRow[m-1]
  
def uniquePaths(m: int, n: int) -> int:
  prevRow = [1] * n
  
  for _ in range(m-1):
    newRow = [1] * n
    for j in range(n-2, -1, -1):
      newRow[j] = newRow[j+1] + prevRow[j]
      
    prevRow = newRow
  
  return prevRow[0]

# grid = [[5, 9, 6], [11, 5, 2]]
grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSumRec(grid))
print(minPathSumMemo(grid))
print(minPathSumTab(grid))
print(minPathSumSO(grid))
from typing import List

# !!! This solution is for learning DP topics, DP is not the best solution to the particular problem

# Find all paths from (0,0) to (n-1,m-1) in a matrix

# Recursive O(2^n*m) SC: O((n-1) + (m-1))
def findAllPathsRec(matrix: List[List[int]]) -> int:
  def helper(i: int, j: int) -> int:
    if i == 0 and j == 0:
      return 1
    
    if i < 0 or j < 0:
      return 0
    
    up = findAllPathsRec(matrix, i-1, j)
    left = findAllPathsRec(matrix, i, j-1)
    
    return up + left
  
  n = len(matrix)
  m = len(matrix[0])
  return helper(n-1, m-1)

# Memoize overlapping subproblems TC: O(n*m) SC: O((n-1) + (m+1)) + O(n*m)
def findAllPathsSO(matrix: List[List[int]]) -> int:
  def helper(i: int, j: int, dp: List[int]):
    if i == 0 and j == 0:
      return 1
    
    if i < 0 or j < 0:
      return 0
    
    if dp[i][j] != -1:
      return dp[i][j]
      
    up = helper(i-1, j, dp)
    left = helper(i, j-1, dp)
    
    dp[i][j] = up + left
    return dp[i][j]
  
  n, m = len(matrix), len(matrix[0])
  dp = [-1 for i in range(m)]
  return helper(n-1, m-1, dp)
  
# Tabulation TC: O(n*m) SC: O(n*m)
def findAllPathsTab(matrix: List[List[int]]) -> int:
  n, m = len(matrix), len(matrix[0])
  dp = [[0 for j in range(m)] for i in range(n)]
  
  dp[0][0] = 1
  
  for i in range(n):
    for j in range(m):
      if i == 0 and j == 0:
        continue
      else:
        if i > 0:
          up = dp[i-1][j]
        if j > 0:
          left = dp[i][j-1]
        dp[i][j] = up + left
  
  return dp[n-1][m-1]


# Space Optimize Recursion
def findAllPathsSO(matrix: List[List[int]]) -> int:
  def helper(i: int, j: int, dp: List[int]):
    if i == 0 and j == 0:
      return 1
    
    if i < 0 or j < 0:
      return 0
    
    if dp[i][j] != -1:
      return dp[i][j]
      
    up = helper(i-1, j, dp)
    left = helper(i, j-1, dp)
    dp[i][j] = up + left
    return dp[i][j]
  
  n, m = len(matrix), len(matrix[0])
  dp = [-1 for i in range(m)]
  return helper(n-1, m-1, dp)
  
# Space Optimize Tabulation
def findAllPathsTab(matrix: List[List[int]]) -> int:
  n = len(matrix)
  m = len(matrix[0])
  prevRow = [0 for _ in range(m)]
  
  for i in range(n):
    currRow = [0 for _ in range(m)]
    for j in range(m):
      if i == 0 and j == 0:
        currRow[j] = 1
      else:
        up, left = 0, 0
        if i > 0:
          up = prevRow[j]
        if j > 0:
          left = currRow[j-1]
        
        currRow[j] = up + left
    # Update previous row for next iteration
    prevRow = currRow
        
  return prevRow[n-1]


from typing import List

# Find all paths from (0,0) to (n-1,m-1) in a matrix

# Recursive O(2^n*m) SC: O((n-1) + (m-1))
def findAllPathsRec(matrix: List[List], i: int, j: int) -> int:
  if i == 0 and j == 0:
    return 1
  
  if i < 0 or j < 0:
    return 0
  
  up = findAllPathsRec(matrix, i-1, j)
  left = findAllPathsRec(matrix, i, j-1)
  
  return up + left

# Memoize overlapping subproblems TC: O(n*m) SC: O((n-1) + (m+1)) + O(n*m)
def findAllPathsRec(matrix: List[List[int]], i: int, j: int, dp: List[List[int]]) -> int:
  if i == 0 and j == 0:
    return 1
  
  if i < 0 or j < 0:
    return 0
  
  if dp[i][j] != -1:
    return dp[i][j]
  
  up = findAllPathsRec(matrix, i-1, j)
  left = findAllPathsRec(matrix, i, j-1)
  
  dp[i][j] = up+left
  return up + left
  
# Tabulation TC: O(n*m) SC: O(n*m)
def findAllPathsTab(matrix: List[List[int]]) -> int:
  n = len(matrix)
  m = len(matrix[0])
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


# Space Optimize

from typing import List

def getMaxPathSum(matrix: List[List[int]]) -> int:
  n = len(matrix)
  m = len(matrix[0])
  
  def f(i: int, j: int) -> int:
    if j < 0 or j >= m:
      return int(-1e9)
    
    if i == 0:
      # We reached the first row starting from row n-1
      return matrix[0][j]
    
    up = matrix[i][j] + f(i-1, j, matrix)
    ld = matrix[i][j] + f(i-1, j-1, matrix)
    rd = matrix[i][j] + f(i-1, j, matrix)
    
    return max(up, ld, rd)
  
  res = int(1e9)
  for j in range(m):
    res = max(res, f(n-1, j))
  
  return res

def getMaxPathSum(matrix: List[List[int]]) -> int:
  n = len(matrix)
  m = len(matrix[0])
  
  def f(i: int, j: int, dp: List[List[int]]) -> int:
    if j < 0 or j >= m:
      return int(-1e9)
    
    if i == 0:
      # We reached the first row starting from row n-1
      return matrix[0][j]
    
    if dp[i][j] != -1:
      return dp[i][j]
    
    up = matrix[i][j] + f(i-1, j, matrix)
    ld = matrix[i][j] + f(i-1, j-1, matrix)
    rd = matrix[i][j] + f(i-1, j, matrix)
    
    dp[i][j] = max(up, ld, rd)
    return dp[i][j]
  
  dp = [[-1 for _ in range(m)] for _ in range(n)]
  res = int(1e9)
  
  for j in range(m):
    res = max(res, f(n-1, j))
  
  return res
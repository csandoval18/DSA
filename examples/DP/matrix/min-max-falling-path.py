from typing import List

# Recursion
def getMaxPathSumRecursion(matrix: List[List[int]]) -> int:
  n = len(matrix)
  m = len(matrix[0])
  
  def f(i: int, j: int) -> int:
    if j < 0 or j >= m:
      return -int(1e9)
    
    if i == 0:
      # We reached the first row starting from row n-1
      return matrix[0][j]
    
    up = matrix[i][j] + f(i-1, j)
    ld = matrix[i][j] + f(i-1, j-1)
    rd = matrix[i][j] + f(i-1, j+1)
    
    return max(up, ld, rd)
  
  res = -int(1e9)
  for j in range(m):
    res = max(res, f(n-1, j))
  
  return res

# Memoization
def getMaxPathSumMemoization(matrix: List[List[int]]) -> int:
  n = len(matrix)
  m = len(matrix[0])
  
  def f(i: int, j: int, dp: List[List[int]]) -> int:
    if j < 0 or j >= m:
      return -int(1e9)
    
    if i == 0:
      # We reached the first row starting from row n-1
      return matrix[0][j]
    
    if dp[i][j] != -1:
      return dp[i][j]
    
    up = matrix[i][j] + f(i-1, j, dp)
    ld = matrix[i][j] + f(i-1, j-1, dp)
    rd = matrix[i][j] + f(i-1, j+1, dp)
    
    dp[i][j] = max(up, ld, rd)
    return dp[i][j]
  
  dp = [[-1 for _ in range(m)] for _ in range(n)]
  res = -int(1e9)
  
  for j in range(m):
    res = max(res, f(n-1, j, dp))
  
  return res
  
# Tabulation
def getMaxPathSumTabulation(matrix: List[List[int]]) -> int:
  n = len(matrix)
  m = len(matrix[0])
  dp = [[0 for _ in range(m)] for _ in range(n)]

  # Initializing the first row of dp as the base condition
  for j in range(m):
    dp[0][j] = matrix[0][j]
  
  # Iterate through the matrix to compute the max path sum
  # Start from 1 since row 0 has been initialized
  for i in range(1, n):
    for j in range(m):
      # Calc the 3 possible moves: up, left diagonal, & right diagonal
      up = matrix[i][j] + dp[i-1][j]
      
      # Handle left diagonal
      ld = matrix[i][j]
      if j > 0:
        ld = matrix[i][j] + dp[i-1][j-1]
      else:
        ld += -int(1e9)
      
      # Handle right diagonal
      rd = matrix[i][j]
      if j < m-1:
        rd = matrix[i][j] + dp[i-1][j+1]
      else:
        rd += -int(1e9)
      
      # Store the max of the 3 moves in dp
      dp[i][j] = max(up, ld, rd)
  
  res = float('-inf')
  for j in range(m):
    res = max(res, dp[n-1][j])
  
  return res
        
    
matrix = [[1, 2, 10, 4], [100, 3, 2, 1], [1, 1, 20, 2], [1, 2, 2, 1]]
print(getMaxPathSumRecursion(matrix))
print(getMaxPathSumMemoization(matrix))
print(getMaxPathSumTabulation(matrix))
 
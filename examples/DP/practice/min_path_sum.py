from typing import List

# Rercusion
def minPathSum(grid: List[List[int]]) -> int:
  n = len(grid)
  m = len(grid[0])
  
  def f(i: int, j: int) -> int:
    if i == n-1 and j == m-1:
      return grid[i][j]
    
    # If we are at the last row, then we can only move right
    if i == n-1:
      return grid[i][j] + f(i, j+1)
    # If we are at the last col, then we can only move down
    if j == m-1:
      return grid[i][j] + f(i+1, j)
    
    return grid[i][j] + min(f(i,j+1), f(i+1, j))
  
  return f(0,0)
  
#  Memoization
def minPathSumMemo(grid: List[List[int]]) -> int:
  n = len(grid)
  m = len(grid[0])
  
  def f(i: int, j: int) -> int:
    if i == n-1 and j == m-1:
      return grid[i][j]
    
    if dp[i][j] != -1:
      return dp[i][j]
  
    if i == n-1:
      return grid[i][j] + f(i, j+1)
    
    if j == m-1:
      return grid[i][j] + f(i+1, j)
    
    dp[i][j] = grid[i][j] + min(f(i, j+1), f(i+1, j))
    return dp[i][j]

  dp = [[-1 for _ in range(m)] for _ in range(n)]
  return f(0,0)

# Attempt at Tabulation 
# def minPathSumTab(grid: List[List[int]]) -> int:
#   n = len(grid)
#   m = len(grid[0])
#   dp = [[0 for _ in range(m)] for _ in range(n)]
  
#   for i in range(n):
#     for j in range(m):
#       if i == n-1 and j == m-1:
#         dp[i][j] = grid[i][j]
      
#       if i == n-1:
#         dp[i][j] = grid[i][j] + dp[i][j+1]
      
#       if j == m-1:
#         dp[i][j] = grid[i][j] + dp[i+1][j]
      
#       dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])
      
#   return dp[n-1][m-1]

# Basically for tabulation we need to keep in track what we actually need to compute the current cell 
# Looking at the previous recursive solutions we can see that we will need the cell on top and the cell on the left

def minPathSumTab(grid: List[List[int]]) -> int:
  n = len(grid)
  m = len(grid[0])
  dp = [[0 for _ in range(m)] for _ in range(n)]
  dp[0][0] = grid[0][0]
  
  for i in range(n):
    for j in range(1, m):
      left = grid[i][j] + dp[i][j-1]
      if i > 0:
        up = grid[i][j] + dp[i-1][j]
      
      dp[i][j] = min(left, up)
      
      
      
      
          
        
        
        
  
  
  
  

grid = [[1,3,1],[1,5,1],[4,2,1]]
print(minPathSum(grid))
print(minPathSumMemo(grid))
print(minPathSumTab(grid))

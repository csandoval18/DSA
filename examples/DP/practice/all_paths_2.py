from typing import List

# def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
def uniquePathsWithObstaclesRec(n: int, m: int) -> int:
  def f(i: int, j: int) -> int:
    if i == n-1 and j == m-1:
      return 1
    
    if i == n-1:
      return f(i, j+1)
    
    if j == m-1:
      return f(i+1, j)
    
    return f(i, j+1) + f(i+1, j)
  
  return f(0, 0)

def uniquePathsWithObstaclesMemo(n: int, m: int) -> int:
  def f(i, j, dp):
    if i == n-1 and j == m-1:
      return 1
    
    if dp[i][j] != -1:
      return dp[i][j]
    
    if i == n-1:
      return f(i, j+1, dp)
    
    if j == m-1:
      return f(i+1, j, dp)
    
    dp[i][j] = f(i, j+1, dp) + f(i+1, j, dp)
    return dp[i][j]
  
  dp = [[-1 for _ in range(m)] for _ in range(n)]
  return f(0, 0, dp)
  

def uniquePathsSO(n: int, m: int) -> int:
  prevRow = [1] * m
  
  for i in range(1, n):
    currRow = [-1] * m
    for j in range(m):
      up = prevRow[j]
      left = 0
      if j > 0:
        left = currRow[j-1]

      currRow[j] = up + left
    prevRow = currRow
  
  return prevRow[m-1]

def uniquePathSO(n: int, m: int) -> int:
  prevRow = [1] * m
  for i in range(n):
    currRow = [0] * m
    for j in range(m):
      up = prevRow[j]
      left = 0
      if j > 0:
        left = currRow[j-1]

      currRow[i] = up + left
    
    prevRow = currRow
  return prevRow[m-1] 
  
def uniquePathsWithObstacles2(obstacleGrid: List[List[int]]) -> int:
  prevRow = [0] * m
  for i in range(1, n):
    currRow = [0] * m
    for j in range(m):
      if obstacleGrid[i][j] == 1:
        
      else:
        continue
      
    
  
n = 3
m = 7
print(uniquePathsWithObstaclesRec(n, m))
print(uniquePathsWithObstaclesMemo(n, m))
print(uniquePathsSO(n, m))

  
from typing import List

# def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
def uniquePathsWithObstacles(n: int, m: int) -> int:
  def f(i: int, j: int) -> int:
    if i == n-1 and j == m-1:
      return 1
    
    if i == n-1:
      return f(i, j+1)
    
    if j == m-1:
      return f(i+1, j)
    
    return f(i, j+1) + f(i+1, j)
  
  return f(0, 0)
  
n = 3
m = 7
print(uniquePathsWithObstacles(n, m))
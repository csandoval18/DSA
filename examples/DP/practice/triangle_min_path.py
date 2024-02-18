from typing import List

def minTotalTriangle(triangle: List[List[int]]) -> int:
  n = len(triangle)
  
  def f(i, j) -> int:
    m = len(triangle[i])
    
    if i == n-1:
      return triangle[i][j]
    
    down = triangle[i][j] + f(i+1, j)
    dr = triangle[i][j] + f(i+1, j+1)
    
    return min(down, dr)
  
  return f(0,0)
  

def minTotalTriangleTabulation(triangle: List[List[int]]) -> int:
  n = len(triangle)
  m = len(triangle[n-1])
  
  dp = [[int(1e9) for _ in range(m)] for _ in range(n)]
  dp[0][0] = triangle[0][0]
  
  for i in range(1, n):
    for j in range(len(triangle[i])):
      top = ld = int(1e9)
      
      # check left diagonal
      if j > 0:
        ld = dp[i-1][j-1]
        
      # check top by seeing if the prev row is in len of j
      if j < len(triangle[i-1]):
        top = dp[i-1][j]
      
      dp[i][j] = triangle[i][j] + min(top, ld)
      
  return min(dp[n-1])
  
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(minTotalTriangle(triangle))
print(minTotalTriangleTabulation(triangle))
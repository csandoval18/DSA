from typing import List

def getMaxPathSum(matrix: List[List[int]]) -> int:
  n = len(matrix)
  m = len(matrix[0])
  
  def rec(i: int, j: int) -> int:
  
  curr_max = int(-1e9)
  
  
  for j in range(m):
    res = max(res, getMaxPathSum(n-1, j, matrix))
  
  
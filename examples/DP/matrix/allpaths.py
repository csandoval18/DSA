from typing import List

# Find all paths from (0,0) to (n-1,m-1) in a matrix

# Recursive O(2^n*m)
def findAllPathsRec(matrix: List[List], i: int, j: int) -> int:
  if i == 0 and j == 0:
    return 1
  
  if i < 0 or j < 0:
    return 0
  
  up = findAllPathsRec(matrix, i-1, j)
  left = findAllPathsRec(matrix, i, j-1)
  
  return up + left


  
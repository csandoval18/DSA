from typing import List


class Solution:
  def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
    if len(original) != m * n:
      return []
      
    grid = [[0]*n for _ in range(m)]
    i = 0
    
    for x in range(m):
      for y in range(n):
        grid[x][y] = original[i]
        i += 1

    return grid
from typing import List


class Solution:
  def minCost(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    
    for i in range(n):
      for j in range(m):
        
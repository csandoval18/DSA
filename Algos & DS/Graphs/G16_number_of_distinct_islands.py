from typing import List

def countDistinctIslands(grid: List[List[int]]) -> int:
  n, m = len(grid), len(grid[0])
  visited = [[False]*m for _ in range(n)]
  
  for i in range(n):
    for j in range(m):
      
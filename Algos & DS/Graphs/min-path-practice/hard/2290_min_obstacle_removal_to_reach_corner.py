from typing import List

# You are given a 0-indexed 2D int array grid of size mxn. Each cell has one of two values:
# 0: Represents an empty cell
# 1: Represents an obstacle that may be removed



class Solution:
  def minimumObstacles(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    dist = [float('inf')]
    dist[0][0] = 0
    pq = [()]

grid = [[0,1,1],
        [1,1,0],
        [1,1,0]]


from heapq import heappop, heappush
from typing import List

# You are given a 0-indexed 2D int array grid of size mxn. Each cell has one of two values:
# 0: Represents an empty cell
# 1: Represents an obstacle that may be removed

# You can move up, down, left, or right from and to an empty cell.

# Return the min number of obstacles to remove so you can move from the upper left 
# corner (0,0) to the lower right corner (m-1, n-1)

class Solution:
  def minimumObstacles(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 0
    pq = [(0,0,0)]
    
    while pq:
      cost, x, y = heappop(pq)
      
      if cost > dist[x][y]:
        continue
      
      for i, (dx, dy) in enumerate([(0,1),(0,-1),(1,0),(-1,0)]):
        nx, ny = dx + x, dy + y
        
        if 0 <= nx < n and 0 <= ny < m:
          # nc = cost + (grid[x][y] != i+1)
          nc = cost + 1 if grid[nx][ny] == 1 else cost
          
          if nc < dist[nx][ny]:
            dist[nx][ny] = nc
            heappush(pq, (nc, nx, ny))
            
    return dist

grid = [[0,1,1],
        [1,1,0],
        [1,1,0]]
# Output: 2
s = Solution()
print(s.minimumObstacles(grid))
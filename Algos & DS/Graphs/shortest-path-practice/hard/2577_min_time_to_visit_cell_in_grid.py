from heapq import heappop, heappush
from typing import List


class Solution:
  def minimumTime(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    dist = [[float('inf')]*m for _ in range(n)]
    dist[0][0] = 0
    pq = [(0,0,0)]
    
    while pq:
      t, x, y = heappop(pq)
      
      if t > dist[x][y]:
        continue
    
      for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx, ny = dx + x, dy + y
        
        if 0 <= nx < n and 0 <= ny < m and dist[x][y] <= dist[nx][ny]:
          nt = t + dist[x][y]
          
          if nt < dist[nx][ny]:
            dist[nx][ny] = nt
            heappush(pq, (nt, nx, ny))
            
      return dist[n-1][m-1] if dist[n-1][m-1] < float('inf') else -1
      
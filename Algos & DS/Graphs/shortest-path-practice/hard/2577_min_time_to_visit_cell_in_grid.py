from heapq import heappop, heappush
from typing import List


class Solution:
  def minimumTime(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    dist = [[float('inf')]*m for _ in range(n)]
    dist[0][0] = 0
    pq = [(0,0,0)] # (time, row, col)
    
    while pq:
      t, x, y = heappop(pq)
      
      if x == n-1 and y == m-1:
        return t
    
      for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx, ny = dx + x, dy + y
        
        if 0 <= nx < n and 0 <= ny < m and dist[x][y] <= dist[nx][ny]:
          nt = t + dist[x][y]
          
          if nt < dist[nx][ny]:
            dist[nx][ny] = nt
            heappush(pq, (nt, nx, ny))
            
      return -1
  
class Solution:
  def minimumTime(self, grid: List[List[int]]) -> int:
    if grid[0][1] > 1 and grid[1][0] > 1:
      return -1
      
    n, m = len(grid), len(grid[0])
    dist = [[float('inf')]*m for _ in range(n)]
    dist[0][0] = 0
    pq = [(0,0,0)] # (t, x, y)
    
    while pq:
      t, x, y = heappop(pq)
      
      if x == n-1 and y == n-1:
        return t
      
      for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx, ny = dx + x, dy + y
        
        if 0 <= nx < n and 0 <= ny < m:
          nt = t + 1
          if nt >= dist[nx][ny]:
            continue
          else:
            if nt - grid[nx][ny] % 2 == 0:
              dist[nx][ny] = max(nt, grid[nx][ny])
            else:
              dist[nx][ny] = max(nt, grid[nx][ny] + 1)
            heappush(pq, (dist[nx][ny], nx, ny))
            
      return -1
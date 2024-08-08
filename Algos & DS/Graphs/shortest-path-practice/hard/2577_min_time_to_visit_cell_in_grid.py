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
    n, m = len(grid), len(grid[0])
    if grid[0][1] > 1 and grid[1][0] > 1:
      return -1
      
    visited = [[False] * n for _ in range(m)]
    heap = [(0, 0, 0)] # (t, r, c)
    
    while heap:
        t, x, y = heappop(heap)
        
        if x == n-1 and y == m-1:
          return t
            
        if visited[x][y]:
          continue
          
        visited[x][y] = True
        
        for dx, dy in [(0,1), (0,-1), (1,0), (-1, 0)]:
          nx, ny = x + dx, y + dy
          
          if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            wait = (grid[nx][ny] - t) % 2 == 0
            nt = max(grid[nx][nx] + wait, t+1)
            heappush(heap, (nt, nx, ny))
    return -1

class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        visited = [[False] * n for _ in range(m)]
        heap = [(0, 0, 0)] # (t, r, c)
        while heap:
            t, r, c = heapq.heappop(heap)
            if r == m - 1 and c == n - 1:
                return t
            if visited[r][c]:
                continue
            visited[r][c] = True
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= m or nc < 0 or nc >= n or visited[nr][nc]:
                    continue
                wait = (grid[nr][nc] - t) % 2 == 0
                nt = max(grid[nr][nc] + wait, t + 1)
                heapq.heappush(heap, (nt, nr, nc))
        return -1
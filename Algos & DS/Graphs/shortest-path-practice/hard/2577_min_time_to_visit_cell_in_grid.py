from heapq import heappop, heappush
from typing import List

class Solution:
  def minimumTime(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    if grid[0][1] > 1 and grid[1][0] > 1:
      return -1
    visited = [[False]*n for _ in range(m)]
    heap = [(0, 0, 0)]

    while heap:
      t, x, y = heappop(heap)
      
      if x == m - 1 and y == n - 1:
        return t
          
      if visited[x][y]:
        continue
      visited[x][y] = True
      
      for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = x+dx, y+dy

        if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
          wait = (grid[nx][ny] - t) % 2 == 0
          nt = max(grid[nx][ny] + wait, t + 1)
          heappush(heap, (nt, nx, ny))
    return -1
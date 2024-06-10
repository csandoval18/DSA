import heapq
from typing import List

class Solution:
  def minimumEffortPath(self, heights: List[List[int]]) -> int:
    n, m = len(heights), len(heights[0])
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 0
    
    # (effort, x, y)
    heap = [(0, 0, 0)]
    
    while heap:
      effort, x, y = heapq.heappop(heap)
      
      # If we reached the bottom-right corner, return the effort
      if x == n - 1 and y == m - 1: # if wt > dist[x][y]:
        return effort # continue
      
      for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, dy + y
        
        if 0 <= nx < n and 0 <= ny < m: # if dist[node] + wt < dist[adjNode]:
          # Calculate new effort based on heights difference
          new_effort = max(effort, abs(heights[nx][ny] - heights[x][y])) # dist[adjNode] = dist[node] + wt    
          
          if new_effort < dist[nx][ny]: # if new_effort < dist[nx]ny]:
            dist[nx][ny] = new_effort # dist[nx][ny] = dist[x][y] + wt
            heapq.heappush(heap, (new_effort, nx, ny)) # heapq.heappush(effort, x, y))

    return dist[n - 1][m - 1]
    
s = Solution()
heights = [[1,2,2],[3,8,2],[5,3,5]]
print(s.minimumEffortPath(heights))
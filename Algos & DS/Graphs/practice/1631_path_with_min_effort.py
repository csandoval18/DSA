import heapq


class Solution: 
  def minimumEffortPath(self, heights: List[List[int]]) -> int:
    n, m = len(heights), len(heights[0])
    dist = [[float('inf') * m] for _ in range(n)]
    dist[0][0] = 0
    
    # (weight, x, y)
    heap = [(0,0,0)]
    
    while heap:
      wt, x, y = heapq.heappop(heap)
      
      if wt > dist[x][y]:
        continue
      
      
      for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx, ny = dx + x, dy + y
        
        if 0 <= nx < n and 0 <= ny < m and dist[x][y] + wt < dist[nx][ny]:
          dist[nx][ny] = dist[nx][ny] + wt
          heapq.heappush(heap, (dist[nx][ny], nx, ny))
          
    return dist
import heapq
from typing import List

# Key:
# 1 = right, 2 = left, 3 = up, 4 = down

# Cases:
# 1. Can move to indicated cell by current cell number.
# 2. Are at a bound at either n-1 or m-1 and must change the cell's number direction

class Solution:
  def minCost(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 0
    pq = [(0, 0, 0)]
    
    while pq:
      cost, x, y = heapq.heappop(pq)
    
      # If we have reached the bottom-right corner
      if x == n-1 and y == m-1:
        return cost
      
      # Skip if the current cost is greater than the recorded cost
      if cost > dist[x][y]:
        continue
      
      for i, (dx, dy) in enumerate([(0,1),(0,-1),(1,0),(-1,0)]):
        nx, ny = dx + x, dy + y
        
        if 0 <= nx < n and 0 <= ny < m: # Calculate the cost to reach the neighbor
          # If the move direction matches the current cell's direction, the cost to move is `cost + 0` (no additional cost)
          # If the move direction does not match, the cost to move is `cost + 1` (an additional cost of 1)
          # This ensures that moving in the indicated direction from a cell is free, while moving in any other direction incurs a cost of 1.
          nc = cost + (grid[x][y] != i+1)
          
          if nc < dist[nx][ny]:
            dist[nx][ny] = nc
            heapq.heappush(pq, (nc, nx, ny))
            
    return dist[n-1][m-1]
    

grid = [
  [1, 1, 3],
  [3, 2, 2],
  [1, 1, 4]
]

s = Solution()
print(s.minCost(grid))  # Output: 0
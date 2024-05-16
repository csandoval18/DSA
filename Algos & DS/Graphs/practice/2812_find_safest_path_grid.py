from typing import List

# 1 = thief
# 0 = empty

def maximumSafenessFactor(grid: List[List[int]]) -> int:
  n = len(grid)

  start = (0,0)
  end = (n-1, n-1)
  
  safest_dist = dijkstra(start, end)
  
  if safest_dist == -1:
    return []
  
  # Backtrack to reconstruct the safest path
  path = [end]
  x, y = end
  

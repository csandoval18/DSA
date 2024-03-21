from collections import deque
from typing import List

# We need to use bfs for this solution since we need to minimize the time
# of infecting other oranges. If we used dfs the time to do this would be maximized 
# since we would need to go through the depth instead of going throw levels 
# checking top, left, right, down per level
def orangesRotting(grid: List[List[int]]) -> List[List[int]]:
  n, m = len(grid), len(grid[0])
  fresh = 0
  queue = deque()
  minutes = 0
  
  # Count fresh oranges and add rotten oranegs to the queue
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 1:
        fresh += 1
      elif grid[i][j] == 2:
        queue.append((i, j, 0))
  
  # BFS tot rot oranges
  while queue:
    x, y, time = queue.popleft()
    minutes = max(minutes, time)
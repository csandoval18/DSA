from collections import deque
from typing import List

def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
  n = len(grid)
  # Early exit if start or end is blocked
  if grid[0][0] != 0 or grid[n-1][n-1] != 0:
    return -1
  
  # Directions array representing 8 possible movements
  # directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
  queue = deque([(0, 0, 1)]) # (x, y, path_length)
  grid[0][0] = 1 # Mark the start cell as visited
  
  while queue:
    x, y, dist = queue.popleft()
    
    # Check if the target is reached
    if x == n-1 and y == n-1:
      return dist
    
    # Nested loop to generate all 8 possible moves
    for dx in [-1, 0, 1]:
      for dy in [-1, 0, 1]:
        # Skip the (0, 0) delta to avoid self-looping
        if dx == 0 and dy == 0:
          continue
        
        nx, ny = x + dx, y + dy
        # Ensure the new position is within bounds and not blocked
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
          queue.append((nx, ny, dist+1))
          grid[nx][ny] = 1 # Mark the cell as visited
          
    return -1 # If no path is found
    
    
def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
  n = len(grid)
  if grid[0][0] != 0 or grid[n-1][n-1] != 0:
    return -1
  
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
  queue = deque(list)
  queue.append((0, 0, 1))
  
  grid[0][0] = 1
  
  while queue:
    x, y, dist = queue.popleft()
    
    # Check if the target is reached
    if x == n-1 and y == n-1:
      return dist
    
    for dx, dy in directions:
      nx, ny = x + dx, y + dy
      
      if 0 <= x < n and 0 <= y < n and grid[nx][ny] == 0:
        queue.append((nx, ny, dist+1))
        grid[nx][ny] = 1
        
  return -1
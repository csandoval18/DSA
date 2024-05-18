from collections import deque
from heapq import heappop, heappush
from typing import List

# 1 = thief
# 0 = empty

def maximumSafenessFactor(grid: List[List[int]]) -> int:
  n = len(grid)
  
  # Initialize a queue to hold the cells to explore
  queue = deque()
  # Iterate through the grid to find cells with value 1 and add them to the queue
  for i in range(n):
      for j in range(n):
          if grid[i][j]:
              queue.append((i, j))
              grid[i][j] = -1  # Mark as visited

  # Initialize a distance variable to track the distance from the start cell
  d = 1
  # Perform BFS traversal to calculate the distance of each cell from the nearest 1
  while queue:
    # Process all cells at the current distance level
    for _ in range(len(queue)):
      x, y = queue.popleft()
      grid[x][y] = d
      # Check adjacent cells and add them to the queue if they are not visited
      for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
          if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
            queue.append((nx, ny))
            grid[nx][ny] = -1  # Mark as visited
    d += 1
    
    # Initialize a min heap to find the shortest path to the end cell
    heap = [(-grid[0][0], 0, 0)] # Use negative values to create a min heap
    
    while heap:
      # Pop the cell with the smallest dist from the heap
      d, x, y = heappop(heap)
      # If the end cell is reached, return the maximum safeness factor
      if x == y == n-1:
          return -d-1  # Return the maximum safeness factor
      # Explore adjacent cells and update the heap
      for nx, ny in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] != -1:
          # Calculate the maximum safeness factor considering the current cell and adjacent cell
          heappush(heap, (max(-grid[nx][ny], d), nx, ny))
          grid[nx][ny] = -1 # Mark as visited
    
    
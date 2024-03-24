from collections import deque
from typing import List

# We need to use bfs for this solution since we need to minimize the time
# of infecting other oranges. If we used dfs the time to do this would be maximized 
# since we would need to go through the depth instead of going throw levels 
# checking top, left, right, down per level

# 2 = Rotten orange
# 1 = Fresh orange (needs to be decomposed)
# 0 = Empty cell (can not be visited)

# This solution does not use a visited array to simplify the solution
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
  
  # BFS to rot oranges
  while queue:
    x, y, time = queue.popleft()
    minutes = max(minutes, time)
    
    # The delta matrix is used to explore the top, left, right, & bottom cells adjacent to the current cell
    delta_matrix = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in delta_matrix:
      nx = x + dx
      ny =  y + dy
      
      if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
        grid[nx][ny] = 2
        fresh -= 1
        queue.append((nx, ny, time+1))
      
  return -1 if fresh != 0 else minutes


# Solution using a visited array
def orangesRottingV2(grid: List[List[int]]) -> List[List[int]]:
  n, m = len(grid), len(grid[0])
  fresh = 0
  minutes = 0
  queue = deque()
  visited = [[False]*m for _ in range(n)]
  
  # Count the fresh oranges and add rotten oranges to the queue
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 2:
        queue.append((i, j, 0))
        visited[i][j] = True # Mark as visited
      elif grid[i][j] == 1:
        fresh += 1
  
  # BFS to rot oranges per levels
  while queue:
    x, y, time = queue.popleft()
    minutes = max(minutes, time)
    
    delta_matrix = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in delta_matrix:
      nx, ny = x + dx, y + dy
      
      # Check if the next x and new y are in range of the matrix boundries
      if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and not visited[nx][ny]:
        grid[nx][ny] = 2 # Update fresh orange found as rotten
        fresh -= 1 # Decrement fresh count
        
        queue.append((nx, ny, time + 1))
        visited[nx][ny] = True # Mark as visited
    
  return -1 if fresh != 0 else minutes

def orangesRottingPrac(grid: List[List[int]]) -> List[List[int]]:
  n, m = len(grid), len(grid[0])
  fresh = 0
  minutes = 0
  queue = deque()
  visited = [[False]*m for _ in range(n)]
  
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 2:
        queue.append(i, j, 0)
        visited[i][j] = True
      elif grid[i][j] == 1:
        fresh += 1
  
  # BFS
  while queue:
    x, y, time = queue.popleft()
    minutes = max(minutes, time)
    
    delta_matrix = [(1,0), (-1,0), (0,1), (0,-1)]
    for dx, dy in delta_matrix:
      nx = x + dx
      ny = y + dy
    
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
        queue.append((nx, ny, time+1))
        visited[nx][ny] = True
  
  return -1 if fresh != 0 else minutes
      
      
  
grid = [
  [2,1,1],
  [1,1,0],
  [0,1,1]
]

print(orangesRotting(grid))

grid = [
  [2,1,1],
  [1,1,0],
  [0,1,1]
]

print(orangesRottingV2(grid))
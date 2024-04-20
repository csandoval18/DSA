from typing import List

def numIslands(grid: List[List[str]]) -> int:
  n, m = len(grid), len(grid[0])
  
  def dfs(x: int, y: int):
    grid[i][j] = -1
    
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
      nx, ny = dx + x, dy + y
      
      if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
        dfs(nx, ny)
    
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 1:
        res += 1
        dfs(i, j)
  return res
  
def numIslands(grid: List[List[str]]) -> int:
  n, m = len(grid), len(grid[0])
  res = 0
  
  def dfs(x: int, y: int):
    # Mark the current cell as visited by setting it to '0'
    grid[x][y] = '0'
    
    # Explore all four possible directions
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
      nx, ny = x + dx, y + dy
      
      # Check bounds and whether the cell is unvisited land
      if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1':
        dfs(nx, ny)
  
  # Iterate over each cell in the grid
  for i in range(n):
    for j in range(m):
      # Start a DFS when an unvisited land cell is found
      if grid[i][j] == '1':
        res += 1
        dfs(i, j)
  return res
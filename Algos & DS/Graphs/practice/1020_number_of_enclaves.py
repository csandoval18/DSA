from typing import List

def numEnclaves(grid: List[List[int]]) -> int:
  n, m = len(grid), len(grid[0])
  enclaves = 0
  visited = [[False]*m for _ in range(n)]
  
  def dfs(x: int, y: int):
    visited[x][y] = True
    
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
      nx, ny = dx + x, dy + y
      
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
        dfs(nx, ny)
  
  for i in range(n):
    if not visited[i][0] and grid[i][0] == 1:
      dfs(i, 0)
    if not visited[i][m-1] and grid[i][m-1] == 1:
      dfs(i, m-1)
  
  for j in range(m):
    if not visited[0][j] and grid[0][j] == 1:
      dfs(0, j)
    if not visited[n-1][j] and grid[n-1][j] == 1:
      dfs(n-1, j)
  
  for i in range(n):
    for j in range(m):
      if not visited[i][j] and grid[i][j] == 1:
        enclaves += 1
  
  return enclaves
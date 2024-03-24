from typing import List

def countDistinctIslands(grid: List[List[int]]) -> int:
  n, m = len(grid), len(grid[0])
  visited = [[False]*m for _ in range(n)] # visited is a local variable 
  # set<vector<pair<int,int>>> st
  distinct_islands = set()
  
  def dfs(x1: int, y1: int, island_pattern: List[(int, int)], x2: int, y2: int):
    visited[i][j] = True
    island_pattern.append((x1-x2, y1-y2))
    
    # delrow = [-1,0,1,0]
    # delcol = [0,-1,0,1]
    delta_matrix = [(1, 0), (-1,0), (0,1), (0,-1)]
    for dx, dy in delta_matrix:
      nrow = x1 + dx
      ncol = x2 + dy
      
      if 0 < nrow <= n and 0 < ncol <= m and not visited[nrow][ncol] and grid[nrow][ncol] == 1:
        dfs(nrow, ncol, island_pattern, x2, y2)
    
  for i in range(n):
    for j in range(m):
      if not visited[i][j] and grid[i][j] == 1:
        island_pattern = []
        dfs(i, j, island_pattern, i, j)
        distinct_islands.add(island_pattern)
      
        

grid = [
  [1, 1, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 1, 1]
]
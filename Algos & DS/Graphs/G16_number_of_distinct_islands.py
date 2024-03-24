from typing import List, Tuple

def countDistinctIslands(grid: List[List[int]]) -> int:
  n, m = len(grid), len(grid[0])
  visited = [[False]*m for _ in range(n)] # visited is a local variable 
  # set<vector<pair<int,int>>> st
  distinct_islands = set()
  
  def dfs(curr_x: int, curr_y: int, island_pattern: List[Tuple[int, int]], ref_x: int, ref_y: int):
    visited[curr_x][curr_y] = True
    island_pattern.append((curr_x-ref_x, curr_y-ref_y))
    
    # delrow = [-1,0,1,0]
    # delcol = [0,-1,0,1]
    delta_matrix = [(1, 0), (-1,0), (0,1), (0,-1)]
    for dx, dy in delta_matrix:
      nrow = curr_x + dx
      ncol = curr_y + dy
      
      if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and grid[nrow][ncol] == 1:
        dfs(nrow, ncol, island_pattern, ref_x, ref_y)
    
  for i in range(n):
    for j in range(m):
      if not visited[i][j] and grid[i][j] == 1:
        island_pattern = []
        dfs(i, j, island_pattern, i, j)
        distinct_islands.add(tuple(island_pattern))
  
  return len(distinct_islands)
      
        
grid = [
  [1, 1, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 1, 1]
]
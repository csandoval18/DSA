from typing import List, Tuple

def countDistinctIslands(grid: List[List[int]]) -> int:
  n, m = len(grid), len(grid[0])
  visited = [[False]*m for _ in range(n)] # visited is a local variable 
  # set<vector<pair<int,int>>> st
  distinct_islands = set() # We use a set to keep track of the distinct islands
  
  # DFS traversal to find the total island "land mass" and marking the visited matrix cells
  def dfs(curr_x: int, curr_y: int, island_pattern: List[Tuple[int, int]], ref_x: int, ref_y: int):
    visited[curr_x][curr_y] = True # Set current cell as visited
    island_pattern.append((curr_x-ref_x, curr_y-ref_y)) # Add the current cell coordinates to island pattern list
    
    # delrow = [-1,0,1,0]
    # delcol = [0,-1,0,1]
    delta_matrix = [(1, 0), (-1,0), (0,1), (0,-1)] # Delta matrix to check up, down, left, right from current cell
    for dx, dy in delta_matrix:
      nrow = curr_x + dx # New row coordinate calculated
      ncol = curr_y + dy # New col coordinate calculated
      
      # Check if the new coordinate of the cell is in range of the matrix, is not already marked as visited, and 
      # the cell is actually a land cell labeled as '1'
      if 0 <= nrow < n and 0 <= ncol < m and not visited[nrow][ncol] and grid[nrow][ncol] == 1:
        dfs(nrow, ncol, island_pattern, ref_x, ref_y) # If the above conditions are met we can continue the dfs traversal
    
  # This loop traverses the entire 
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
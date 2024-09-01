from typing import List

class Solution:
  def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    m, n = len(grid1), len(grid1[0])
    
    def dfs(x: int, y: int):
      is_sub_island = True # Assume it's a sub island until proven false
      grid2[x][y] = 0 # Mark as visited
      
      for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx, ny = dx + x, dy + y
        
        # Check if next position is within bounds
        if 0 <= nx < m and 0 <= ny < n and grid2[nx][ny] == 1:
          # Recurse for next cell
          if not dfs(nx, ny):
            is_sub_island = False
            
      # Check if grid1 does not have an island at the same position
      if grid1[x][y] == 0:
        is_sub_island = False
        
      return is_sub_island
    
    sub_islands = 0
    for x in range(m): 
      for y in range(n):
        if grid2[x][y] == 1:
          if dfs(x, y):
            sub_islands += 1
    return sub_islands
    
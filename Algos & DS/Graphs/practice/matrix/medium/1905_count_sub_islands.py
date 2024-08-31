from typing import List

class Solution:
  def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
    m, n = len(grid1), len(grid1[0])
    
    def dfs(x: int, y: int):
      is_sub_island = True # Assume it's a sub island until proven false
      grid2[x][y] = 0 # Mark as visited
      
      for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
        nx, ny = dx + dx, dy + y
        
        # Check if next position is within bounds
      

    for x in range(m): 
      for y in range(n):
        if grid2[x][y] == 1:
          if dfs(x, y):
            sub_islands += 1
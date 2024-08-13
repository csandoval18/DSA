from typing import List


class Solution:
  def minDays(self, grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    def is_not_connected():
      visited = [[False]*n for _ in range(m)]
      
      # The logic to check if the island is connected is by using a dfs and change the first island mass into visited
      # The second nested loop then traverses again through the matrix. If an island cell is found that is not visited,
      # then the island is not connected and we return True
      def dfs(x: int, y:int) -> bool:
        if 0 <= x < m and 0 <= y < n and not visited[x][y] and grid[x][y] == 1:
          visited[x][y] = True
          for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            dfs(x+dx, y+dy)
        
      # Find any land cells to start dfs
      for x in range(m):
        for y in range(n):
            if grid[x][y] == 1:
              dfs(x, y)
              # Check if all 1s were visited
              for x1 in range(m):
                for y1 in range(n):
                  if grid[x1][y1] == 1 and not visited[x1][y1]:
                    return True
              return False
      return True # No land is found, therefore it is disconnected

    if is_not_connected(): return 0 # Initial island is already disconnected
    
    # Try removing each land cell and check connectivity:
    for x in range(m):
      for y in range(n):
        if grid[x][y] == 1:
          grid[x][y] = 0
          if is_not_connected():
            return 1
          grid[x][y] = 1
          
    return 2
    
    
      
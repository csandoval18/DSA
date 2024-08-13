from typing import List


class Solution:
  def regionsBySlashes(self, grid: List[str]) -> int:
    n = len(grid)
    # Initiate a expanded grid from 2x2 to 6x6 since each char index turn into a 3x3 grid
    matrix = [[0] * (n*3) for _ in range(n*3)] 
    m = len(matrix)
    
    for x in range(n):
      for y in range(n):
        if grid[x][y] == '/':
          matrix[x*3][y*3+2] = 1 # Add +2 to y go to the end of the last column of the 3x3 block
          matrix[x*3+1][y*3+1] = 1 # Add +1 to go to the middle of the column and row of the 3x3 block
          matrix[x*3+2][y*3] = 1
        elif grid[x][y] == '\\': 
          matrix[x*3][y*3] = 1
          matrix[x*3+1][y*3+1] = 1
          matrix[x*3+2][y*3+2] = 1
          
    def dfs(x: int, y: int): # Perform dfs to explore regions
      if 0 <= x < m and 0 <= y < m and matrix[x][y] == 0:
        matrix[x][y] = 1 # Mark cell as visited
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
    
    regions = 0
    for x in range(n*3):
      for y in range(n*3):
        if matrix[x][y] == 0:
          dfs(x, y)
          regions += 1
    
    return regions
        

grid = [" /",
        "/ "]

# Grid:
# [" ","/"]
# ["/"," "]

# Expanded Grid:
# [0,0,0,0,0,1]
# [0,0,0,0,1,0]
# [0,0,0,1,0,0]
# [0,0,1,0,0,0]
# [0,1,0,0,0,0]
# [1,0,0,0,0,0]

# Output: 2
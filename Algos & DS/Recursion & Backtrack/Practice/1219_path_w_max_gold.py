from typing import List

def getMaximumGold(grid: List[List[int]]) -> int:
  n, m = len(grid), len(grid[0])
  
  def dfs(x: int, y: int, curr_gold: int):
    if x < 0 or x >= n or y < 0 or y >= m or grid[x][y] == 0:
      return
      
    gold = grid[x][y]
    grid[x][y] = 0 # Mark current cell as visited
    
    # Calc new gold amount including current cell
    curr_gold += gold
    # Explore all four directions nd keep track of max gold found
    max_gold = 0
    
    for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)]:
      max_gold = max(max_gold, dfs(x + dx, y + dy, curr_gold))
    
    # Backtrack: unmark this cell as visited
    grid[x][y] = gold
    curr_gold -= gold
    
    return max_gold
    
  res = 0
  
  for i in range(n):
    for j in range(m):
      if grid[i][j] > 0: # Start dfs if the cell has gold
        res = max(res, dfs(i, j, 0))
  
  return res

grid = [
  [0, 6, 0],
  [5, 8, 7],
  [0, 9, 0]
]

print(getMaximumGold(grid))  # Expected output depends on the grid layout

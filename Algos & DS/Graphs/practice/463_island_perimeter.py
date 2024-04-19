from typing import List

# dfs
def islandPerimeter(grid: List[List[int]]) -> int:
  n, m = len(grid), len(grid[0])
  
  def dfs(x: int, y: int):
  # If the cell is out of bounds or water, it contributes 1 to the perimeter
    if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] == 0:
      return 1
    
    # If the cell is already visited, it contributes 0 to the perimeter
    if grid[x][y] == -1:
      return 0
    
    # Mark the cell as visited
    grid[x][y] = -1

    # Recursively calculate the perimeter contribution from all four directions
    perimeter = dfs(x+1, y)
    perimeter += dfs(x-1, y)
    perimeter += dfs(x, y+1)
    perimeter += dfs(x, y-1)
    
    return perimeter
  
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 1:
        # Start DFS from the first land cell found
        return dfs(i, j)
  
  return 0 # If no land is found

def islandPerimeterDM(grid: List[List[int]]) -> int:
  n, m = len(grid), len(grid[0])
  
  def dfs(x: int, y: int):
    # Base case: if we're out of boundsor the cell is water, it adds to the perimeter
    if x < 0 or y < 0 or x >= n or y >= m or grid[x][y] == 0:
      return 1
    
    # If the cell is already visited, it doesn't contribute to the perimeter
    if grid[x][y] == -1:
      return 0
    
    # Mark the cell as visited
    grid[x][y] = -1
    perimeter = 0
    
    # Recursively calculate perimeter using delta matrix for directions
    for dr, dc in delta:
      perimeter += dfs(x + dr, y + dc)
    
    return perimeter
  
  # Find first land cell to start dfs
  for i in range(n):
    for j in range(m):
      if grid[i][j] == 1:
        return dfs(i, j)
  
  return 0

grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
print(islandPerimeter(grid))  # Output: 16
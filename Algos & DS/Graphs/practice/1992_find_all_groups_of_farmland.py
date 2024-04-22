from typing import List

def findFarmland(land: List[List[int]]) -> List[List[int]]:
  n, m = len(land), len(land[0])
  res = []
  
  def dfs(i: int, j: int, coordinates: List[int]):
    # Check out of bounds and wether the cell is already processed or is not farmland
    if i < 0 or i >= n or j < 0 or j >= m or grid[i][j] != 1:
      return
    
    # Mark this cell as visited by setting it to 0
    land[i][j] = 0
    
    # Update the coordinates with the enw edges
    coordinates[2] = max(coordinates[2], i) # Bottom-most row
    coordinates[3] = max(coordinates[3], j) # Right-most column
    
    # Explore the neighbors (right and down only to extend the rectangle)
    dfs(i+1, j, coordinates)
    dfs(i, j+1, coordinates)
    
  # Iterate over all cells in the grid
  for i in range(n):
    for j in range(m):
      if land[i][j] == 1:
        # Initialize coordinates as [top, left, bottom, right]
        coordinates = [i, j, i, j]
        dfs(i, j, i, j)
        # Append the rectangle's top-left and bottom-right corners
        res.append([coordinates[0], coordinates[1], coordinates[2], coordinates[3]])
        
  return res
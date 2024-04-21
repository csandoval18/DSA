from typing import List

def findFarmland(land: List[List[int]]) -> List[List[int]]:
  n, m = len(land), len(land[0])
  
  def dfs(i: int, j: int, coordinates: List[int]):
    # Check out of bounds and wether the cell is already processed or is not farmland

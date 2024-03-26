from typing import List

def isCyclic(V: int, adj: List[List[int]]) -> bool:
  visited = [False]*V
  pathVis = [False]*V
  
  def dfs(node: int) -> bool:
    visited[node] = True
    pathVis[node] = True
    
    # Traverse for adj nodes
    
  
  for node in range(V):
    if not visited[node]:
      if dfs(node):
        return True
  return False
  
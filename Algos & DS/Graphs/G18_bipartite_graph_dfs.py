from typing import List

def isBipartite(V: int, adj: List[List[int]]) -> bool:
  color = [-1] * V
  
  def dfs(node: int, curr_color: int) -> bool:
    color[node] = curr_color
    
    for adjNode in adj[node]:
      if color[adjNode] == -1:
        # if dfs(adjNode, 1 if curr_color == 0 else 0) == False:
        if dfs(adjNode, 1 - color[node]) == False:
          return False
      elif color[adjNode] == curr_color:
        return False
    return True
  
  for node in range(V):
    if color[node] == -1:
      if not dfs(node, 0):
        return False
  return True
  
  
  #  dfs(1, 0)
  #   /        \ 
  # dfs(2, 1)     
  # dfs()
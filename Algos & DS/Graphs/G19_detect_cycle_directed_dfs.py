from typing import List

def isCyclic(V: int, adj: List[List[int]]) -> bool:
  visited = [False]*V
  pathVis = [False]*V
  
  def dfs(node: int) -> bool:
    visited[node] = True
    pathVis[node] = True
    
    for adjNode in adj[node]:
      if not visited[adjNode]:
        if dfs(adjNode):
          return True
      # If the node has been visited and visited on the same path,
      # then there is a cycle present
      elif pathVis[adjNode]:
        return True
        
    pathVis[node] = False
    return False
    
  for node in range(V):
    if not visited[node]:
      if dfs(node):
        return True
  return False
  
def isCyclic(V: int, adj: List[List[int]]) -> bool:
  visited = [False]*V
  pathVis = [False]*V
  
  def dfs(node: int) -> bool:
    visited[node] = True
    pathVis[node] = True
    
    for adjNode in adj[node]:
      if not visited[adjNode]:
        if dfs(adjNode):
          return True
      elif pathVis[adjNode]: 
        return True
  
  for node in range(V):
    if not visited[node]:
      if dfs(node):
        return True
  return False
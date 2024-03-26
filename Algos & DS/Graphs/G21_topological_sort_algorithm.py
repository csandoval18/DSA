from typing import List

def topoSort(V: int, adj:List[List[int]]) -> List[int]:
  visited = [False]*V
  stack = []
  
  def dfs(node: int) -> None:
    visited[node] = True
    
    for adjNode in adj[node]:
      if not visited[adjNode]:
        dfs(adjNode)
        
    stack.append(node)
  
  for node in range(V):
    if not visited[node]:
      dfs(node)
  
  return stack[::-1]
    
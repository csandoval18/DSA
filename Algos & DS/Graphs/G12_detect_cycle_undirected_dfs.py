from typing import List

# TC: O(N+2E)
# SC: O(N)
def isCycle(V: int, adj: List[List[int]]) -> List[int]:
  visited = [False] * V
  
  def dfs(node: int, parent: int):
    visited[node] = True
    
    for adjNode in adj[node]:
      if not visited[adjNode]:
        if dfs(adjNode, node):
          return True
      elif parent != adjNode:
        return True
    
    return False
    
  for node in range(V):
    if not visited[node]:
      if dfs(node, -1):
        return True
  return False
  
from collections import deque
from typing import List

# DFS traversal
def dfsOfGraph(v: int, adj: List[List[int]]) -> List[int]:
  def dfs(node: int) -> List[int]:
    visited[node] = True
    res.append(node) # Append node 0 (starting node)
    
    for neighbor in adj[node]: # Traverse all neighbors
      if not visited[neighbor]:
        dfs(neighbor)
        
  # Mark all the vertices as not visited
  visited = [False]*v
  start = 0
  res = []
  dfs(start)
  return res


def dfsOfGraph(V: int, adj: List[List[int]]) -> List[int]:
  vis = [False]*V
  start = 0
  res = []
  
  def dfs(u: int) -> List[int]:
    vis[u] = True
    res.append(u)
    
    for v in adj[u]:
      if not vis[v]:
        dfs(v)
  
  dfs(start)
  return res

# TC: O(N) + O(2xE)
v = 5        
adj = [[2,3,1] , [0], [0,4], [0], [2]]
print(dfsOfGraph(v, adj))
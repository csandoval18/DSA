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
  visited = [False]*V
  start = 0 
  res = []
  
  def dfs(node: int) -> List[int]:
    visited[node] = True
    res.append(node)
    
    for neighbor in adj[node]:
      if not visited[neighbor]:
        dfs(neighbor)
  
  dfs(start)
  return res

def dfsOfGraph(V: int, adj: List[List[int]]) -> List[int]:
  visited = [False]*V
  start = 0
  res = []
  
  def dfs(node: int) -> List[int]:
    visited[node] = True
    res.append(node)
    
    for adjNode in adj[node]:
      if not visited[adjNode]:
        dfs(adjNode)
  
  dfs(start)
  return res
    

# TC: O(N) + O(2xE)
v = 5        
adj = [[2,3,1] , [0], [0,4], [0], [2]]
print(dfsOfGraph(v, adj))
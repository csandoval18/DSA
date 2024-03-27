# Topological Sorting (Kahn's Algorithm | BFS) 

# 1. Insert all nodes with indegree 0

from collections import deque
from typing import List

def topoSort(V: int, adj: List[List[int]]) -> bool:
  indegree = [0]*V
  topo = []
  
  for node in range(V):
    for adjNode in adj[node]:
      indegree[adjNode] += 1 

  queue = deque()
  for node in range(V):
    if indegree[node] == 0:
      queue.append(node)
  
  while queue:
    node = queue.popleftf()
    topo.append(node)
    
    for adjNode in adj[node]:
      
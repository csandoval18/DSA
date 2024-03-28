# Topological Sorting (Kahn's Algorithm | BFS) 

# 1. Insert all nodes with indegree 0

from collections import deque
from typing import List

def topoSort(V: int, adj: List[List[int]]) -> bool:
  indegree = [0]*V
  topo = []
  
  # Compute the indegree for every node by traversing adjacency list
  for node in range(V):
    for adjNode in adj[node]:
      indegree[adjNode] += 1 

  # We start with the nodes that have 0 indegrees appended to queue
  queue = deque()
  for node in range(V):
    if indegree[node] == 0:
      queue.append(node)
  
  # Traverse graph 
  while queue:
    node = queue.popleft()
    topo.append(node)
    
    # Node is in the topo sort, so it must be removed from the indegree
    for adjNode in adj[node]:
      indegree[adjNode] -= 1 # Decrement indegree of adjacent nodes
      if indegree[adjNode] == 0: # If the adjacent node indegree is 0, then add it to the queue
        queue.append(adjNode)
  
  return topo
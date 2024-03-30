from collections import deque
from typing import List

def isCyclic(V: int, adj: List[List[int]]) -> bool:
  indegree = [0]*V
  # topo = []
  topo_count = 0
  
  for node in range(V):
    for adjNode in adj[node]:
      indegree[adjNode] += 1
  
  queue = deque()
  for node in range(V):
    if indegree[node] == 0:
      queue.append(node)
  
  while queue:
    node = queue.popleft()
    # topo.append(node)
    topo_count += 1
    
    for adjNode in adj[node]:
      indegree[adjNode] -= 1
      if indegree[adjNode] == 0:
        queue.append(adjNode)
    
  if topo_count == V:
    return False
  return True
  
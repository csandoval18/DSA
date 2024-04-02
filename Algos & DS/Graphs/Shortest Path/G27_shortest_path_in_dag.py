from collections import defaultdict
from typing import List

def shortestPath(n : int, m : int, edges: List[List[int]]) -> List[int]:
  adj = defaultdict(list)
  for i in range(m):
    u, v, wt = edges[i]
    adj[u].append((v, wt))

  visited = [False]*n
  stack = []
  
  def dfsTopoSort(node):
    visited[node] = True
    
    for adjNode in adj[node]:
      v = adjNode[0]
      if not visited[v]:
        dfsTopoSort(v)
        
    stack.append(node)  # Use list as a stack, append/push to end

  for node in range(n):
    if not visited[node]:
      dfsTopoSort(node)

  dist = [float('inf')] * n
  dist[0] = 0

  while stack:
    node = stack.pop()  # Pop from end of list to simulate stack

    if dist[node] != float('inf'):
      for adjNode in adj[node]:
        v, wt = adjNode
        if dist[node] + wt < dist[v]:
          dist[v] = dist[node] + wt

  # Replace 'inf' with -1 to indicate no path
  dist = [-1 if x == float('inf') else x for x in dist]
  return dist
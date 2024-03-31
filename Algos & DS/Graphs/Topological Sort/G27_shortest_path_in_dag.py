from typing import List


def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
  adj = [[] for _ in range(n)]
  topo = []
  
  # Create graph holding (vertex, weight)
  for i in range(n):
    u = edges[i][0]
    v = edges[i][1]
    wt = edges[i][2]
    adj[u].append((v, wt))
  
  # Find the topo sort
  visited = [False]*n
  stack = []
  
  def dfs_topo_sort(node: int):
    visited[node] = True
  
    for node in range(n):
      v = node[0]
      if not visited[node]:
        dfs_topo_sort(v)
    
    topo.append(node)
  
  # Step 2: do the distance calculations
  dist = [float('inf')]*n
  dist[0] = 0
  
  while stack:
    node = stack.pop()
    
    for node in adj[node]:
      v = node[0]
      wt = node[1]
      
      if dist[node] + wt < dist[v]:
        dist[v] = dist[node] + wt
  return dist
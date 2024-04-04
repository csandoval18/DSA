# The Bellman Ford Algorithm unlike the dijkstra algorithm does work in graphs with negative edges.
# This algorithm only works in directed graphs
# BF finds negative cycles

# dist[u] + wt < dist[v]

# 1. Why n-1 iterations?


# 2. How to detect negative cycles?

from typing import List


# TC: O(VxE) 
def bellman_ford(V: int, edges: List[List[int]], S: int) -> List[int]:
  dist = [float('inf')]*V
  dist[S] = 0
  
  for _ in range(V-1):
    for u, v, wt in edges:
      if dist[u] != float('inf') and dist[u] + wt < dist[v]:
        dist[v] = dist[u] + wt
  
  # Nth relaxation to check for negative cycles
  for u, v, wt in edges:
    if dist[u] != float('inf') and dist[u] + wt < dist[v]:
      return [-1] # If a negative cycle is detected, return -1
  
  return dist
  
  
def bellman_ford_geeksforgeeks(V: int, edges: List[List[int]], S: int) -> List[int]:
  dist = [int(1e8)]*V
  dist[S] = 0
  
  for _ in range(V-1):
    for u, v, wt in edges:
      if dist[u] != int(1e8) and dist[u] + wt < dist[v]:
        dist[v] = dist[u] + wt
  
  for u, v, t in edges:
    if dist[u] != int(1e8) and dist[u] + wt < dist[v]:
      return [-1]
  
  return dist
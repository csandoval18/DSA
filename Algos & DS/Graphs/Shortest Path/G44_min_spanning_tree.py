# A spanning tree has N nodes and N-1 edges
# Intuition: This algorithm is GREEDY

# Ex:
# 0 - 1 - 2     5 nodes
#   / |         4 edges
#  3  4

from ast import List
import heapq

# O(E + log(E))
def spanningTree(V: int, adj: List[List[int]]):
  visited = [False]*V
  pq = [(0,0)]
  total_weight = 0
  
  while pq:
    wt, node = heapq.heappop(pq)
    
    if visited[node]:
      continue
    
    visited[node] = True
    total_weight += wt
    
    for adjNode, edW in adj[node]: # Keep in mind that in the adj list the order is (node, weight) for the tuple
      if not visited[adjNode]:
        heapq.heappush(pq, (edW, adjNode))
    
  return total_weight
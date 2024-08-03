from heapq import heappop, heappush
from typing import List

# You are given an integer n denoting the number of nodes of a weighted directed graph.
# The nodes are numbered from 0 to n - 1.

class Solution:
  def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
    adj = [[] for _ in range(n)]
    
    for u, v, w in edges:
      adj[u].append((v, w))
    
    def dijkstra(source: int) -> List[int]:
      dist = [float('inf')]*n
      dist[source] = 0
      pq = [(0, source)]
      
      while pq:
        uw, u = heappop(pq)
        
        if uw > dist[u]:
          continue
      
        for v, vw in adj[u]:
          nw = uw + vw
          
          if nw < dist[v]:
            dist[v] = nw
            heappush(pq, (nw, v))
      
      return dist
  
  
          
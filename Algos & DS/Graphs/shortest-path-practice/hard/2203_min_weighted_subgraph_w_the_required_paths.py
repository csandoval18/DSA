from heapq import heappop, heappush
from typing import List

# You are given an integer n denoting the number of nodes of a weighted directed graph.
# The nodes are numbered from 0 to n - 1.

class Solution:
  def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
    def dijkstra(adj: List[List[int]], source: int) -> List[int]:
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
      
    g = [[] for _ in range(n)]
    rev_g = [[] for _ in range(n)]
    
    for u, v, w in edges:
      g[u].append((v, w))
      rev_g[v].append((u, w))
  
    dist1 = dijkstra(g, src1)
    dist2 = dijkstra(g, src2)
    dist3 = dijkstra(rev_g, dest)
    
    res = float('inf')
    for i in range(n):
      if dist1[i] < float('inf') and dist2[i] < float('inf') and dist3[i] < float('inf'):
        res = min(res, dist1[i] + dist2[i] + dist3[i])
    return res if res != float('inf') else -1
from heapq import heappop, heappush
from typing import List


class Solution:
  def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
    adj = [[] for _ in range(n)]
    for u, v, cnt in edges:
      adj[u].append((v, cnt))
      adj[v].append((u, cnt))
    
    dist = [float('inf')]*n
    dist[0] = 0
    pq = [(cnt, 0)]
    visited = [False]*n
    
    while pq:
      ucnt, u = heappop(pq)
      
      if visited[u]:
        continue
      visited[u] = True
      
      for v, vcnt in adj[u]:
        if v not in visited: 
          ncnt = ucnt + vcnt + 1
          
          if ncnt < dist[v]:
            dist[v] = ncnt
            heappush(pq, (ncnt, v))
            
    reachable_nodes = 0
    for d in dist:
      if d <= maxMoves:
        reachable_nodes += 1
    
    for u, v, cnt in edges:
      reach_u = max(0, maxMoves - dist[u])
      reach_v = max(0, maxMoves - dist[v])
      reachable_nodes += min(cnt, reach_u + reach_v)
    
    return reachable_nodes
from collections import defaultdict
import heapq
from typing import List


class Solution:
  def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    adj = defaultdict(list)
    for u, v, w in edges:
      adj[u].append((v, w))
      adj[v].append((u, w))

    dist = [float('inf')]*n
    dist[0] = 0
    pq = [(0, 0)]
    
    while pq:
      uw, u = heapq.heappop(pq)
      
      if uw > dist[u]:
         continue
      
      for v, vw in adj[u]:
        nw = uw + vw
        
        if nw < dist[u]:
          dist[v] = nw
          heapq.heappush((nw, v))
          
    
    min_cnt = float('inf')
    
    
  
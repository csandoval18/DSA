from collections import defaultdict
import heapq
from typing import List


# k = dest
class Solution:
  def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    adj = defaultdict(list)
    for u, v, w in times:
      adj[u].append((v, w))
    
    pq = [(0, k)]
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0
    
    while pq:
      curr_dist, u = heapq.heappop(pq)
      
      if curr_dist > dist[u]:
        continue
      
      for v, w in adj[u]:
        new_dist = curr_dist + w
        if new_dist < dist[v]:
          dist[v] = new_dist
          heapq.heappush(pq, (new_dist, v))
  
    max_dist = max(dist.values())
    return max_dist if max_dist < float('inf') else -1
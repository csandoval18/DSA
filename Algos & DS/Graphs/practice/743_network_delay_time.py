from collections import defaultdict
import heapq
from typing import List


# k = dest
class Solution:
  def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    adj = defaultdict(list)
    
    for u, v, w in times:
      adj[u].append((v, w))
    
    dist = [float('inf')]*n
    dist[k] = 0
    
    pq = [(0, k)]
    while pq:
      time, u = heapq.heappop(pq)
      
      if time > dist[u]:
        continue
    
    for v, w in adj[u]:
      new_time = time + w
      if new_time < dist[v]:
        heapq.heappush(pq, (new_time, v))
    
    max_dist = max(dist)
    return max_dist if max_dist < float('inf') else -1
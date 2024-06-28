from collections import defaultdict
import heapq
from typing import List


class Solution:
  def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    adj = defaultdict(list)
    for u, v, w in edges:
      adj[u].append((v, w))
      adj[v].append((u, w))


    def dijkstra(source: int) -> List[int]:
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
            
      return dist
      
    min_v_cnt = float('inf')
    res_city = -1

    for i in range(n):
      dist = dijkstra(i)
      v_cnt = sum(1 for j in range(n) if dist[j] <= distanceThreshold and i != j)
      
      if  v_cnt < min_v_cnt or (v_cnt == min_v_cnt and i > res_city):
        min_v_cnt = v_cnt
        res_city = i
    
    return res_city
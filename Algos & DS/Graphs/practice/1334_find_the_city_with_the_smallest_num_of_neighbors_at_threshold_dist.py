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
    
class FloydWarshall:
  def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
      dist[i][i] = 0

    # Fill initial distances from edges
    for u, v, w in edges:
      dist[u][v] = w
      dist[v][u] = w
    
    # Floyd-Was
    for k in range(n):
      for u in range(n):
        for v in range(n):
          if dist[u][v] > dist[u][k] + dist[k][v]:
            dist[u][v] = dist[u][k] + dist[k][v]
    
    # Find the city with the smallest number of neighbors within the distance threshold
    min_v_cnt = float('inf')
    res_city = -1
    
    for u in range(n):
      # v_cnt = sum(1 for j in range(n) if dist[u][v] <= distanceThreshold and u != v)
      v_cnt = 0
      for v in range(n):
        if dist[u][v] <= distanceThreshold and u != v:
          v_cnt += 1
      
      if v_cnt < min_v_cnt or (v_cnt == min_v_cnt and u > res_city):
        min_v_cnt = v_cnt
        res_city = u
    
    return res_city



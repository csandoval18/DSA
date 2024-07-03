from collections import defaultdict
import heapq
from typing import List


class Solution:
  def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
    adj = defaultdict(list)
    for u, v, w in edges:
      adj[u].append((v, w))
      adj[v].append((u, w))
    
    def dijkstra(start: int) -> List[int]:
      dist = [float('inf')]*(n+1)
      dist[start] = 0
      pq = [(0, 0)]
      
      while pq:
        uw, u = heapq.heappop(pq)
        
        if uw > dist[u]:
          continue
          
        for v, vw in adj[u]:
          nw = uw + vw
          
          if nw < dist[v]:
            dist[v] = nw
            heapq.heappush(pq, (nw, v))
      return dist
    
    dist = dijkstra(n)
    # dp = {}
    dp =[-1] * (n+1)
    MOD = 10**9 + 7
    
    def dfs(u: int):
      if u == n:
        return 1
      elif u in dp:
        return dp[u]
      
      total_paths = 0
      for v, vw in adj[u]:
        if dist[u] > dist[v]: # Restricted path condition
          total_paths += dfs(v)
          total_paths %= MOD 
      
      dp[u] = total_paths 
      return total_paths
  
    return dfs(1)
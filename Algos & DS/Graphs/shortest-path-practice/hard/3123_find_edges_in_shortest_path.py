from heapq import heappop, heappush
from typing import List

# You are given an undirected weighted graph of n nodes numbered from 0 to n-1. 
# The graph consists of m edges represented by a 2D array edges, where edges[i] = [a, b, w] 
# indicates that there is an edge between nodes



class Solution:
  def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
    adj = [[] for _ in range(n)]
    
    for u, v, w in edges:
      adj[u].append((v, w))
      adj[v].append((u, w))
      
    dist = [float('inf')]*n
    dist[n-1] = 0
    pq = [(0, n-1)]
    res = [False]*n
    
    while pq:
      uw, u = heappop(pq)
      
      if uw > dist[u]:
        continue
        
      for v, vw in adj[u]:
        nw = uw + vw
        
        if nw < dist[v]:
          dist[v] = nw
          heappush(pq, (nw, v))
    
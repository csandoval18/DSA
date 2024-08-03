from collections import defaultdict
from heapq import heappop, heappush
from typing import List

# You are given an undirected weighted graph of n nodes numbered from 0 to n-1. 
# The graph consists of m edges represented by a 2D array edges, where edges[i] = [a, b, w] 
# indicates that there is an edge between nodes

class Solution:
  def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
    adj = [[] for _ in range(n)]
    for i, (u, v, w) in enumerate(edges):
      adj[u].append((v, w, i))
      adj[v].append((u, w, i))
      
    parent = defaultdict(set)
    pq = [(0,0)]
    dist = [float('inf')]*n        
    dist[0] = 0
    
    while pq:
      uw, u = heappop(pq)

      if uw > dist[u]:
        continue
      
      for v, vw, i in adj[u]:
        nw = uw + vw
        
        if nw <= dist[v]:
          if nw < dist[v]:
            dist[v] = nw
            parent[v].clear()
          parent[v].add((u, i))
          heappush(pq, (nw, v))
    
    result = [False] * len(edges)
    def dfs(node: int):
      if node == 0:
        return
      
      for p, i in parent[node]:
        result[i] = True
        dfs(p)
      return
    
    dfs(n - 1)
    return result

class Solution1:
  def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    def dijkstra(source):
      pq = [(0, source)]
      dist = [float('inf')] * n
      dist[source] = 0
      
      while pq:
        uw, u = heappop(pq)
        if uw != dist[u]:
          continue
        
        for v, vw in adj[u]:
          nw = uw + vw
          
          if nw < dist[v]:
            dist[v] =  nw
            heappush(pq, (nw, v))
      return dist
    
    source_dist = dijkstra(0)
    target_dist = dijkstra(n-1)
    
    if n-1 not in source_dist:
      return [False] * len(edges)
      
    min_w = source_dist[n-1]
    ans = []
    for u, v, w in edges:
        if source_dist[u] + w + target_dist[v] == min_w \
            or source_dist[v] + w + target_dist[u] == min_w:
            ans.append(True)
        else:
            ans.append(False)
    return ans

n = 6
edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]
# Output: [true,true,true,false,true,true,true,false]
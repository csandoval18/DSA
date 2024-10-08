from collections import defaultdict
from heapq import heappop, heappush
from typing import List

# You are given an undirected weighted graph of n nodes numbered from 0 to n-1. 
# The graph consists of m edges represented by a 2D array edges, where edges[i] = [a, b, w] 
# indicates that there is an edge between nodes ai and bi with weight wi.

# Consider all the shortest paths from node 0 to node n - 1 in the graph. You need to find a
# boolean array answer where answer[i] is true if the edge edges[i] is part of at least
# one shortest path. Otherwise, answer[i] is false.

# Return the array answer.
# Note that the graph may not be connected.

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
    
    def dijkstra(source: int) -> List[int]: 
      dist = [float('inf')]*n
      dist[source] = 0 
      pq = [(0, source)]
      while pq: 
        uw, u = heappop(pq)
        
        # Notice we dont use the usual check of  "if uw > dist[u]" to skip processing a node that has already been relaxed to a better distance.
        
        # Why not "uw > dist[u]"?
        # - Guaranteeing Relaxation: By ensurering that "uw == dist[u]", we guarantee that we're processing a node whose distance has 
        #   just been finalized. This means any adjacent nodes can be safely relaxed without the risk of processing a node with an 
        #   outdated distance.
        # - Avoiding Duplicate Processing: Without this check, it's possible to process the same node multiple times with different tentative
        #   distance, leading to unnecessary computations.
        # - Optimizing Priority Queue: By only processing nodes with finalized distances, we effectively reduce the number of elements 
        #   in the priority queue, improving its performance.
        
        if uw == dist[u]: 
          for v, vw in adj[u]: 
            nw = uw + vw
            if nw  < dist[v]: 
              dist[v] = nw
              heappush(pq, (nw, v))
      return dist 
    
    dist0, dist1 = dijkstra(0), dijkstra(n-1)
    min_dist = dist0[n-1]
    res = []
    for u, v, w in edges: # Remember the problems requires to check if the edges are 
      if min_dist < float('inf') and (dist0[u] + w + dist1[v] == min_dist or dist0[v] + w + dist1[u] == min_dist):
        res.append(True)
      else:
        res.append(False)
        
    return res
    
    # return [dist0[n-1] < float('inf') and 
    # (dist0[u] + w + dist1[v] == dist0[n-1] or 
    # dist0[v] + w + dist1[u] == dist0[n-1]) 
    # for u, v, w in edges]


n = 6
edges = [[0,1,4],[0,2,1],[1,3,2],[1,4,3],[1,5,1],[2,3,1],[3,5,3],[4,5,2]]
# Output: [true,true,true,false,true,true,true,false]
s = Solution1()
print(s.findAnswer(n, edges))
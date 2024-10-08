from collections import defaultdict
import heapq
from typing import List

# There is an undirected graph of n nodes. 
# You are given a 2D array edges, where edges[i] = [ui, vi, lengthi] describes an edge 
# between node ui and node vi with a traversal time of lengthi units.

# Additionally, you are given an array disappear, where disappear[i] denotes the time 
# when the node i disappears from the graph and you won't be able to visit it.

# Notice that the graph might be disconnected and might contain multiple edges.

# Return the array answer, with answer[i] denoting the minimum units of time required to reach node i from node 0. 
# If node i is unreachable from node 0 then answer[i] is -1.

class Solution:
  def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
    adj = [[] for _ in range(n)]
    for u, v, l in edges:
      adj[u].append((v, l))
      adj[v].append((u, l))
    
    dist = [float('inf')] * n
    dist[0] = 0
    pq = [(0, 0)]
    
    while pq:
      ul, u = heapq.heappop(pq)
      
      if ul > dist[u]:
        continue
        
      for v, vl in adj[u]:
        nl = ul + vl
        
        if nl < dist[v] and nl < disappear[v]:
          dist[v] = nl
          heapq.heappush(pq, (nl, v))
    
    # res = [-1 if dist[i] == float('in') or dist[i] > disappear[i] else dist[i] for i in range(n)]
    res = []
    for i in range(n):
      if dist[i] == float('inf') or dist[i] > disappear[i]:
        res.append(-1)
      else:
        res.append(dist[i])
        
    return res
  

class Solution:
  def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
    adj = [[] for _ in range(n)]
    for u, v, l in edges:
      adj[u].append((v, l))
      adj[v].append((u, l))
    
    dist = [float('inf')] * n
    dist[0] = 0
    pq = [(0, 0)]
    
    

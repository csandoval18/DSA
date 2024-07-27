from heapq import heappop, heappush
from typing import List


class Solution:
  def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
    adj = [[] for _ in range(n)]
    
    for u, v, w in roads:
      adj[u].append((v, w))
      adj[v].append((u, w))
      
    dist = [float('inf')]*n
    dist[0] = 0
    pq = [(0,0)]
    
    while pq:
      uw, u = heappop(pq)
      
      if uw > dist[u]:
        continue
        
      for v, vw in adj[u]:
        nw = uw + vw 
        
        if nw < maxDistance and nw < dist[v]:
          dist[v] = nw
          heappush(pq, (nw, v))
    
    return dis
          
        

n = 3
maxDistance = 5
roads = [[0,1,2],[1,2,10],[0,2,10]]
# Output: 5
# Explanation: The possible sets of closing branches are:
# - The set [2], after closing, active branches are [0,1] and they are 
#   reachable to each other within distance 2.
# - The set [0,1], after closing, the active branch is [2].
# - The set [1,2], after closing, the active branch is [0].
# - The set [0,2], after closing, the active branch is [1].
# - The set [0,1,2], after closing, there are no active branches.
# It can be proven, that there are only 5 possible sets of closing branches.
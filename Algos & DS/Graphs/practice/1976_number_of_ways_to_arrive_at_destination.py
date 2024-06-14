from collections import defaultdict
import heapq
from typing import List


# u = current node
# v = adjacent node / neighbor
# utime = current node weight/time
# vtime = cost of traversing to adjacent v node

class Solution:
  def countPaths(self, n: int, roads: List[List[int]]) -> int:
    MOD = 10**9 + 7
    
    # Create adjacency with bidirectional edges
    adj = defaultdict(list)
    for u, v, time in roads:
      adj[u].append((v, time))
      adj[v].append((u, time))
      
    # Dijkstra's algorithm to find the shortest path
    dist = [float('inf')]*n
    dist[0] = 0
    pq = [(0, 0)]
    ways = {i: 0 for i in range(n)}
    ways[0] = 1
    
    while pq:
      u, utime = heapq.heappop(pq)
      
      # Skip if the popped distance is greater than the recorded shortest distance in dist array
      if utime > dist[u]:
        continue
        
      for v, vtime in adj[u]:
        # ntime = utime + vtime
        if utime + vtime < dist[v]: # Found a shorter parth to the neighbor
          dist[v] = utime + vtime
          ways[v] = ways[u]
          heapq.heappush(pq, (utime + vtime))
        # Found another shortest path tot he neighbor
        elif utime == dist[v]:
          ways[v] = (ways[v] + ways[u]) % MOD

    return ways[n-1]
    
    
class Solution:
  def countPaths(self, n: int, roads: List[List[int]]) -> int:
    MOD = 10**9 + 7
    
    # Create adjacency list
    adj = defaultdict(list)
    for u, v, t in roads:
      adj[u].append((v, t))
      adj[v].append((u, t))  # Assuming undirected roads, add both directions
    
    # Dijkstra's algorithm to find the shortest paths
    pq = [(0, 0)]  # (distance, node)
    dist = [float('inf')]*n
    dist[0] = 0
    ways = [0]*n # Declare ways list to keep track of count of ways to reach the ith node
    ways[0] = 1

    while pq:
      utime, u = heapq.heappop(pq)
      
      # Skip if the popped distance is greater than the recorded shortest distance
      if utime > dist[u]:
        continue
      
      # Explore neighbors
      for v, vtime in adj[u]:
        # dist = vtime + utime
        # Found a shorter path to the neighbor
        if utime + vtime  < dist[v]:
          dist[v] = utime + vtime
          ways[v] = ways[u]  # Reset ways to the new shortest path
          heapq.heappush(pq, (vtime, v))
        # Found another shortest path to the neighbor
        elif utime + vtime == dist[v]:
          ways[v] = (ways[v] + ways[u]) % MOD
          
    return ways[n-1]
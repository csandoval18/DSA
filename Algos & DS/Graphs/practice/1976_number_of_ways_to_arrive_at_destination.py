from collections import defaultdict
import heapq
from typing import List

# This is a Dijkstra and DP problem. We use Dijkstra to find the min path, and DP to keep trak of number of ways to reach a node

# u = current node
# v = adjacent node / neighbor
# utime = current node weight/time
# vtime = cost of traversing to adjacent v node

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
          heapq.heappush(pq, (vtime + utime, v))
        # Found another shortest path to the neighbor
        elif utime + vtime == dist[v]:
          ways[v] = (ways[v] + ways[u]) % MOD
          
    return ways[n-1]

class Solution:
  def countPaths(self, n: int, roads: List[List[int]]) -> int:
    MOD = 10**9+7

    adj = defaultdict(list)
    for u, v, t in roads:
      adj[u].append((v, t))
      adj[v].append((u, t))

    dist = [float('inf')]*n
    dist[0] = 0
    ways = [0]*n
    ways[0] = 1
    pq = [(0, 0)]

    while pq:
      ut, u = heapq.heappop(pq)

      if ut > dist[u]:
        continue
      
      for v, vt in adj[u]:
        if ut + vt < dist[v]: # Checking for a shorter path to v
          dist[v] = ut + vt
          ways[v] = ways[u]  # Update ways[v] to the num of ways to reach u because now the shortest path to v goes through u
          heapq.heappush(pq, (ut + vt, v))
        elif ut + vt == dist[v]:
          ways[v] = (ways[v] + ways[u]) % MOD
    return ways[n-1]
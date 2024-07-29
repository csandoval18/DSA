from collections import defaultdict, deque
from heapq import heappop, heappush
from typing import List

# A city is represented as a bi-directional connected graph with n vertices where each vertex
# is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer
# array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between
# vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex
# has an edge to itself. The time taken to traverse any edge is time minutes.

# Each vertex has a traffic signal which changes its color from green to red and vice versa
# every change minutes. All signals change at the same time. You can enter a vertex at any
# time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

# The second minimum value is defined as the smallest value strictly larger than the minimum value.

# For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.

# Intuition
# Hard problem.
# Since each move takes the same time, it's no need for a priority queue, just a regular queue which holding the info pair (node, distance).

# Since it's to find the 2nd min path, it needs 2 containers, say dist, dist2 to hold the distance to the starting node 1.

class Solution:
  def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
    adj = [[] for _ in range(n)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)
    
    # Priority queue to store the times (time, node, count of paths found)
    pq = [(0,1,0)]
    best_times = {i: [float('inf'), float('inf')] for i in range(1, n + 1)}
    best_times[1][0] = 0
    
    while pq:
      ut, u, path_cnt = heappop(pq)
      
      # Check for traffic light effect
      if (ut // change) % 2 == 1:
        curr_time += (change - curr_time % change) 
    
      for v in adj[u]:
        nt = curr_time + time
        
        if nt < best_times[v][0]:
          best_times[v][1] = best_times[v][0]
          best_times[v][0] = nt
          heappush(pq, (nt, v, path_cnt + 1))
        elif best_times[v][0] < nt < best_times[v]:
          best_times[v][1] = nt
          heappush(pq, (nt, v, path_cnt + 1))
          
    return best_times[n][1]
    
    
class Solution1:
  def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
    g = [[] for _ in range(n + 1)]
    for u, v in edges:
      g[u].append(v)
      g[v].append(u)

    q = deque([(1, 1)])
    dist1 = [-1] * (n + 1)
    dist2 = [-1] * (n + 1)
    dist1[1] = 0
    
    while q:
      x, freq = q.popleft()
      t = dist1[x] if freq == 1 else dist2[x]

      if (t // change) % 2:
        t = change * (t // change + 1) + time

      else:
        t += time

      for y in g[x]:
        if dist1[y] == -1:
          dist1[y] = t
          q.append((y, 1))
        elif dist2[y] == -1 and dist1[y] != t:
          if y == n:
            return t
            
          dist2[y] = t
          q.append((y, 2))
    return 0
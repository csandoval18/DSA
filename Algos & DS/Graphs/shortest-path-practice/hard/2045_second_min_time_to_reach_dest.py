from collections import defaultdict
from heapq import heappop, heappush
from typing import List


class Solution:
  def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
    adj = [[] for _ in range(n)]
    for u, v in edges:
      adj[u].append(v)
      adj[v].append(u)
    
    # Priority queue to store the times (time, node, count of paths found)
    pq = [(0,1,0)]
    best_times = defaultdict(lambda: [float('inf'), float('inf')])
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
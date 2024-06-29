from collections import defaultdict
import heapq
from typing import List


class Solution:
  def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    adj = defaultdict(list)
    for (u, v), prob in zip(edges, succProb):
      adj[u].append((v, prob))
      adj[v].append((u, prob))
    
    dist = [0.0]*n
    dist[start_node] = 1.0
    pq = [(-1.0, start_node)]
    
    while pq:
      uprob, u = heapq.heappop(pq) 
      uprob = -uprob
      
      if u == end_node:
        return uprob
        
      for v, vprob in adj[u]:
        nprob = uprob * vprob
        
        if nprob > dist[v]:
          dist[v] = nprob
          heapq.heappush(pq, (-nprob, v))
    
    return 0.0

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
s = Solution()
print(s.maxProbability(n, edges,succProb, start, end))
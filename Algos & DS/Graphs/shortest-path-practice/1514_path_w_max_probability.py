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

class Solution:
  def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    adj = [[] for _ in range(n)]
    for (u, v), w in zip(edges, succProb):
      adj[u].append((v, w))
      adj[v].append((u, w))
    
    dist = [0.0]*n
    dist[start_node] = 1.0
    pq = [(-1.0, start_node)] # This pq is working as a max heap so we need to turn the weight negative to achieve that functionality
    
    while pq:
      uw, u = heapq.heappop(pq)
      
      if u == end_node:
        return uw
      
      for v, vw in adj[u]:
        nw = uw * vw
        
        if nw > dist[v]:
          dist[v] == nw
          heapq.heappush(pq, (-nw, v))
    
    return 0.0
  

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
s = Solution()
print(s.maxProbability(n, edges,succProb, start, end))
from collections import defaultdict
import heapq
from typing import List


class Solution:
  def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    def dijkstra(s_char: str, t_char: str) -> int:
      n = len(source) # same as target len
      
      # (original, changed, cost)
      adj = defaultdict(list)
      for u, v, swap_cost in zip(original, changed, cost):
        adj[u].append((v, swap_cost))
      
      pq = [(0, s_char)]
      min_cost = {char: float('inf') for char in adj}
      min_cost[source] = 0
      
      while pq:
        ucost, u = heapq.heappop(pq)
        
        if u == t_char:
          return ucost
          
        if ucost > min_cost[u]:
          continue
        
        for v, vcost in adj[u]:
          ncost =  ucost + vcost
          if ncost < min_cost[v]:
            min_cost[v] = ncost
            heapq.heappush(pq, (ncost, v))
            
      return float('inf')
    
    total_min_cost = 0
    for s_char, t_char in zip(source, target):
      if s_char != t_char:
        conversion_cost = dijkstra(s_char, t_char) 
        if conversion_cost == float('inf'):
          return -1
        total_min_cost += conversion_cost
    
    return total_min_cost
          
      
    
    
source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]
s = Solution()
print(s.minimumCost(source, target, original, changed, cost))
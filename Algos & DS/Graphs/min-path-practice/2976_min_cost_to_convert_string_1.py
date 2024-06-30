from collections import defaultdict
import heapq
from typing import List


class Solution:
  def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    def dijkstra(x, y, hm):
      if (x, y) in hm:
        return hm[(x, y)]
        
      pq, visited = [], set()
      heapq.heappush(pq, (0, x))
      
      while pq:
        ucost, u = heapq.heappop(pq)
        
        if u == y:
          return ucost
        if u in visited:
          continue
        visited.add(u)
        
        for v, vcost in adj[u]:
          ncost = ucost + vcost
          heapq.heappush(pq, (ncost, v))                  
      return -1
    
  
    n = len(source)
    adj = defaultdict(list)
    for o, c, co in zip(original, changed, cost):
      adj[o].append([c, co])
    
    res = 0  
    hm = {}
    
    for i in range(n):
      val = dijkstra(source[i], target[i], hm)
      if val == -1:
        return -1
      else:
        res += val
      hm[(source[i], target[i])] = val
    
    return res

class Solution:
  def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    adj = defaultdict(list)  
    for u, v, swap_cost in zip(original, changed, cost):
      adj[u].append((swap_cost, v))
    
    lc_chars = [chr(ord('a') + i) for i in range(26)]
    dist = defaultdict(lambda: float("inf"))
    
    for s in lc_chars:
      pq = [(0, s)]
      dist[(s, s)] = 0
      
      while pq:
        distance, vertex = heapq.heappop(pq)
        
        if dist[(s, vertex)] != distance:  # Outdated value
          continue
        
        for weight, neighbour in adj[vertex]:
          if distance + weight < dist[(s, neighbour)]:
            dist[(s, neighbour)] = distance + weight
            heapq.heappush(pq, (distance + weight, neighbour))
        
    min_cost = 0
    for i in range(len(source)):
      min_cost += dist[(source[i], target[i])]
    
    return min_cost if min_cost != float("inf") else -1
      
source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]
s = Solution()
print(s.minimumCost(source, target, original, changed, cost))
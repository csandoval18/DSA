from collections import defaultdict
import heapq
from typing import List


class Solution:
  def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
    n = len(original)
    adj = defaultdict(list)
    
    for u, v, c in zip(original, changed, cost):
        adj[u].append((v, c))
    
    lc_chars = [chr(ord('a') + i) for i in range(26)]
    # The line dist = defaultdict(lambda: float('inf')) initializes dist as a defaultdict 
    # with a default factory function that returns float('inf'). This means that if you try 
    # to access a key in dist that does not exist, it will automatically return float('inf').
    dist = defaultdict(lambda: float('inf'))

    for s in lc_chars:
      pq = [(0, s)]
      dist[(s, s)] = 0
      
      while pq:
        uc, u = heapq.heappop(pq)
        
        if uc != dist[(s, u)]:
          continue
            
        for v, vc in adj[u]:
          nc = uc + vc
          
          if nc < dist[(s, v)]:
            dist[(s, v)] = nc
            heapq.heappush(pq, (nc, v))
    
    min_cost = 0
    for i in range(len(source)):
      if dist[(source[i], target[i])] == float('inf'):
        return -1
      min_cost += dist[(source[i], target[i])]
    
    return min_cost
  

class SolutionOptimized:
  def minCost(original, changed, cost, source, target):
    def char_to_index(c):
      return ord(c) - ord('a')
      
    n = len(original)
    adj = [[] for _ in range(26)]
    
    for u, v, c in zip(original, changed, cost):
      ui = char_to_index(u)
      vi = char_to_index(v)
      adj[ui].append((vi, c))
    
    dist = [[float('inf')] * 26 for _ in range(26)]
    
    for s in range(26):
      pq = [(0, s)]
      dist[s][s] = 0
      
      while pq:
        uc, u = heapq.heappop(pq)
        
        if uc != dist[s][u]:
          continue
            
        for v, vc in adj[u]:
          nc = uc + vc
          
          if nc < dist[s][v]:
            dist[s][v] = nc
            heapq.heappush(pq, (nc, v))
  
    min_cost = 0
    for i in range(len(source)):
      si = char_to_index(source[i])
      ti = char_to_index(target[i])
      
      if dist[si][ti] == float('inf'):
        return -1
      min_cost += dist[si][ti]
    
    return min_cost

# Example usage
original = ['a', 'b', 'c']
changed = ['b', 'c', 'd']
cost = [1, 2, 3]
source = ['a', 'b']
target = ['c', 'd']
s = Solution()
print(s.minCost(original, changed, cost, source, target))  # Output: 3

source = "abcd"
target = "acbe"
original = ["a","b","c","c","e","d"]
changed = ["b","c","b","e","b","e"]
cost = [2,5,5,1,2,20]
s = Solution()
print(s.minimumCost(source, target, original, changed, cost))
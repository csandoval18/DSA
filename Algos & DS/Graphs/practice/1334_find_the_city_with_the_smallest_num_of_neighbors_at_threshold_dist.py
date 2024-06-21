from collections import defaultdict
from typing import List


class Solution:
  def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    adj = defaultdict(list)
    for u, v, w in edges:
      adj[u].append((v, w))
      adj[v].append((u, w))
    
    
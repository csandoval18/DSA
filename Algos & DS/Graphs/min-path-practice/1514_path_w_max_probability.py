from collections import defaultdict
from typing import List


class Solution:
  def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
    adj = defaultdict(list)
    for (u, v), prob in edges:
      adj[u].append(v)
    
    dist = [float('inf')]*n
    dist[start_node] = 0
    pq = [(0, start_node)]
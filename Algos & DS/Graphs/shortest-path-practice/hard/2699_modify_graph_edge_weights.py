from typing import List


class Solution:
  def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
    adj = [[] for _ in range(n)]
    for u,v,w in edges:
      adj[u].append((v, w))
      adj[v].append((v, w))
    
    
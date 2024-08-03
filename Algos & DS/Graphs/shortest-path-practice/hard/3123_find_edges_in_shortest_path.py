from heapq import heappop, heappush
from typing import List

# You are given an undirected weighted graph of n nodes numbered from 0 to n-1. 
# The graph consists of m edges represented by a 2D array edges, where edges[i] = [a, b, w] 
# indicates that there is an edge between nodes

class Solution:
  def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
    graph = defaultdict(list)
    for i, (a, b, w) in enumerate(edges):
      graph[a].append((b, w, i))
      graph[b].append((a, w, i))
      
    parent = defaultdict(set)
    queue = []
    queue.append((0, 0))
    dist = [inf] * n        
    dist[0] = 0
    
    while queue:
      d, node = heappop(queue)

      if d > dist[node]:
        continue
      
      for child, w, i in graph[node]:
        new_d = w + d
        if new_d <= dist[child]:
          if new_d < dist[child]:
            dist[child] = new_d
            parent[child].clear()
          parent[child].add((node, i))
          heappush(queue, (new_d, child))
  
    result = [False] * len(edges)
    def dfs(node):
      if node == 0:
        return
      
      for p, i in parent[node]:
        result[i] = True
        dfs(p)
      return
    
    dfs(n - 1)
    return result
from heapq import heappop, heappush
from typing import List

# You are given an integer n denoting the number of nodes of a weighted directed graph.
# The nodes are numbered from 0 to n - 1.

class Solution:
  def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
    def dijkstra(adj: List[List[int]], source: int) -> List[int]:
      dist = [float('inf')]*n
      dist[source] = 0
      pq = [(0, source)]
      
      while pq:
        uw, u = heappop(pq)
        
        if uw > dist[u]:
          continue
      
        for v, vw in adj[u]:
          nw = uw + vw
          
          if nw < dist[v]:
            dist[v] = nw
            heappush(pq, (nw, v))
      
      return dist
      
    g = [[] for _ in range(n)]
    rev_g = [[] for _ in range(n)]
    
    for u, v, w in edges:
      g[u].append((v, w))
      rev_g[v].append((u, w))
  
    dist1 = dijkstra(g, src1)
    dist2 = dijkstra(g, src2)
    dist3 = dijkstra(rev_g, dest)
    
    res = float('inf')
    for u in range(n):
      if dist1[u] < float('inf') and dist2[u] < float('inf') and dist3[u] < float('inf'):
        res = min(res, dist1[u] + dist2[u] + dist3[u])
    return res if res != float('inf') else -1

n = 6
edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]]
src1 = 0
src2 = 1
dest = 5

# Output: 9
# Explanation:
# The above figure represents the input graph.
# The blue edges represent one of the subgraphs that yield the optimal answer.
# Note that the subgraph [[1,0,3],[0,5,6]] also yields the optimal answer.
# It is not possible to get a subgraph with less weight satisfying all the constraints.
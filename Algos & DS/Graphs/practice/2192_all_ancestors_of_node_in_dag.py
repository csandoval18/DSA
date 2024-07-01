from collections import defaultdict
from typing import List


class Solution:
  def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    rev_adj = defaultdict(list)
    for u, v in edges:
      rev_adj[v].append(u)
    
    ancestors = [set() for _ in range(n)]
    
    def dfs(start: int, u: int):
      for v in rev_adj[u]:
        if v not in ancestors[u]:
          ancestors[u].add(v)
          dfs(node)
    
    for node in range(n):
      dfs(node)
    
    res = [sorted(list(anc)) for anc in ancestors]
    return res

n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
s = Solution()
print(s.getAncestors(n, edgeList))
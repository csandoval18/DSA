from collections import defaultdict, deque
from typing import List


class SolutionDFS:
  def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    rev_adj = defaultdict(list)
    for u, v in edges:
      rev_adj[v].append(u)
    
    ancestors = [set() for _ in range(n)]
    
    def dfs(start: int, u: int):
      for v in rev_adj[u]:
        if v not in ancestors[start]:
          ancestors[start].add(v)
          dfs(start, v)
    
    for node in range(n):
      dfs(node, node)
    
    res = [sorted(list(anc)) for anc in ancestors]
    return res

class SolutionBFS:
  def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    
    rev_adj = defaultdict(list) 
    for u, v in edges:
      rev_adj[v].append[u]
    
    ancestors = [set() for _ in range(n)]
    
    for node in range(n):
     q = deque([node]) 
     vis = set()
     
     while q:
      u = q.popleft()
      
      for v in rev_adj[u]:
        if v not in vis:
          vis.add(v)
          ancestors[u].add(v)
          q.append(v)
    
    result = [sorted(list(ancestor_set)) for ancestor_set in ancestors]
    return result          
          

class Solution:
  def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
    adj = [[] for _ in range(n)]

    for u, v in edges:
      adj[v].append(u)

    ancestors = [None] * n

    def dfs(node):
      if ancestors[node] is not None:
        return ancestors[node]

      result = set()

      for parent in adj[node]:
        result.add(parent)
        result.update(dfs(parent))

      ancestors[node] = sorted(result)
      return ancestors[node]

    for node in range(n):
      dfs(node)

    return ancestors
    

n = 8
edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
s = Solution()
print(s.getAncestors(n, edgeList))
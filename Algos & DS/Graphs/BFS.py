from collections import deque
from typing import List

# Works for directed and undirected graphs
def BFS(V: int, adj: List[List[int]]) -> List[int]:
  visited = [0]*V
  queue = deque()
  bfs = []
  
  visited[0] = 1
  queue.append(0)
  
  while queue:
    node = queue.popleft()
    bfs.append(node)
    
    for neightbor in adj[node]:
      if not visited[neightbor]:
        visited[neightbor] = 1
        queue.append(neightbor)
  return bfs
  
def bfs(v: int, adj: List[List[int]]) -> List[int]:
  visited  = [0]*v
  
  

V = 5
E = 4
adj = [[1,2,3],[],[4],[],[]]
print(BFS(V, adj))
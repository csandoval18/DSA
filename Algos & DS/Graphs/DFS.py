from collections import deque
from typing import List

def DFS(V: int, adj: List[List[int]]) -> List[int]:
  visited = [0]*V
  queue = deque()
  dfs = []
  
  visited[0] = 1
  queue.append(0)
  
  while queue:
    node = queue.popleft()
    dfs.append(node)
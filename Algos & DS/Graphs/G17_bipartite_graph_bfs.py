from collections import deque
from typing import List

# If the graph contains a cycle with odd number of nodes within a cycle
# then the graph is non-bartite

def isBipartite(V: int, adj: List[List[int]]) -> bool:
  color = [-1] * V
  
  def bfs(start: int) -> bool:
    queue = deque()
    queue.append(start)
    
    while queue:
      node = queue.popleft()
      
      for adjNode in adj[node]:
        # If the adj node is yet not colored you will give the opposite color of the node
        if color[adjNode] == -1:
          # color[adjNode] = 1 if color[node]  == 0 else 0
          color[adjNode] = 1 - color[node]
          queue.append(adjNode)
        # If the adjacent node has the same color, another node colored the node in another path
        elif color[adjNode] == color[node]:
          return False
        
    return True
  
  for node in range(V):
    if color == -1:
      if not bfs(node):
        return False
  return True

# Leetcode Variant
def isBipartiteLC(graph: List[List[int]]) -> bool:
  V = len(graph)
  color = [-1] * V
  
  def bfs(start: int) -> bool:
    queue = deque()
    queue.append(start)
    
    while queue:
      node = queue.popleft()
      
      for adjNode in graph[node]:
        if color[adjNode] == -1:
          color[adjNode] = 1 if color[node] == 0 else 0
          queue.append(adjNode)
        elif color[adjNode] == node[adjNode]:
          return False
  return True
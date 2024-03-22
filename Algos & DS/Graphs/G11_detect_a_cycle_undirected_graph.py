from collections import deque
from typing import List

def detect(src: int, adj: List[int], visited: List[bool]) -> bool:
  visited[src] = 1
  queue = deque()
  queue.push((src, -1))
  
  while queue:
    node, parent = queue.popleft()
    
    for adjNode in adj[node]:
      if not visited[adjNode]: # If not visited add to queue and mark as visited
        visited[adjNode] = True
        queue.push(adjNode, node)
      else: # If the adjacent node has been visited, a cycle is detected
        
        
      


def isCycle(V: int, adj: List[List[int]]) -> bool:
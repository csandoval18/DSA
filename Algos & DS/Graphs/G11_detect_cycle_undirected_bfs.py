from collections import deque
from typing import List

# TC: O(V+E)
def detect(src: int, adj: List[int], visited: List[bool]) -> bool:
  visited[src] = 1
  queue = deque()
  queue.append((src, -1))
  
  while queue:
    node, parent = queue.popleft()
    
    for adjNode in adj[node]:
      if not visited[adjNode]: # If not visited add to queue and mark as visited
        visited[adjNode] = True
        queue.append((adjNode, node))
      elif parent != adjNode: # If one of the adjacent nodes is visited but it did not come from the same parent, then there is a cycle
        return True
      
  return False
        
        
def isCycle(V: int, adj: List[List[int]]) -> bool:
  visited = [False] * V
  
  # Traverse all node since the input adjacency list might have unconnected components
  for node in range(V):
    if not visited[node]:
      if detect(node, adj, visited):
        return True
  
  return False


def isCycle(V: int, adj: List[List[int]]) -> bool:
  visited = [False] * V
  
  def detectCycle(src: int) -> bool:
    queue = deque()
    queue.append((src, -1))
    
    while queue:
      currNode, parent = queue.popleft()
      
      for adjNode in adj[currNode]:
        if not visited[adjNode]:
          queue.append((adjNode, currNode))
          visited[adjNode] = True
        elif parent != adjNode:
          return True
    return False
  
  
  for node in range(V):
    if not visited[node]:
      if detectCycle(node):
        return True
  return False
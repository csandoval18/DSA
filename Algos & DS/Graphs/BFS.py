from collections import deque
from typing import List

# Works for directed and undirected graphs
def BFS(V: int, adj: List[List[int]]) -> List[int]:
  visited = [False]*V
  queue = deque()
  bfs = []
  
  visited[0] = 1
  queue.append(0)
  
  while queue:
    node = queue.popleft()
    bfs.append(node)
    
    for neightbor in adj[node]:
      if not visited[neightbor]:
        visited[neightbor] = True
        queue.append(neightbor)
  return bfs
  
def bfs(v: int, adj: List[List[int]]) -> List[int]:
  visited = [False]*v 
  queue = deque()
  bfs = []
  
  # Mark starting node as visited
  visited[0] = 1
  # Insert starting node to queue
  queue.append(0)
  
  # Traverse queue while it's not empty
  while queue:
    # Pop in FIFO order 
    node = queue.popleft()
    # Append node value to bfs answer list
    bfs.append(node)
    
    # Loop to explore for adjacent nodes
    for neightbor in adj[node]:
      # Check if neighbor has not already been visited
      if not visited[neightbor]: 
        # Since the neighbor node has not been visied, then we can mark it as visited
        # and append the node to the queue to visit its neighbors in the next iterations
        visited[neightbor] = True
        queue.append(neightbor)
    
  return bfs
      
def bfs(v: int, adj: List[List[int]]) -> List[int]:
  visited = [False]*v
  queue = deque()
  bfs = []
  
  visited[0] = True
  queue.append(0)
  
  while queue:
    node = queue.popleftf()
    bfs.append(node)
    
    for neighbor in adj[node]:
      if not visited[neighbor]:
        visited[neighbor] = True
        queue.append(neighbor)
    
  return bfs

def bfs(v: int, adj: List[List[int]]) -> List[int]:
  visited = [False]*v
  queue = deque()
  bfs = []
  
  visited[0] = True
  queue.append(0)
  
  while queue:
    node = queue.popleft()
    bfs.append(node)
    
    for neighbor in adj[node]:
      if not visited[neighbor]:
        visited[neighbor] = True
        queue.append(neighbor)
    
  return bfs

def bfs(v: int, adj: List[List[int]]) -> List[int]:
  visited = [False]*v
  queue = deque()
  bfs = []
  
  visited[0] = True
  queue.append(0)
  
  while queue:
    node = queue.popleft()
    bfs.append(node)
    
    for neighbors in adj[node]:
      if not visited[neighbors]:
        visited[neighbors] = True
        queue.append(neighbors)
  
  return bfs
        

V = 5
E = 4
adj = [[1,2,3],[],[4],[],[]]
print(BFS(V, adj))




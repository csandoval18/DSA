from ast import List
from collections import defaultdict, deque

def shortestPath(edges: List[List[int]], n: int, m: int, src: int):
  # Create adjacency list of size N for storing the undirected graph
  adj = [[] for _ in range(n)]
  
  for u, v in edges: # Since the graph is undirected both nodes have a path to each other
    adj[u].append(v)
    adj[v].append(u)
    
  # A dist array of size N initialised with a large number to indicate that initially all the nodes are untraversed.
  dist = [float('inf')]*n
  dist[src] = 0
  
  # BFS Implementation
  queue = deque()
  queue.append(src)
  
  while queue:
    node = queue.popleft()
    
    for adjNode in adj[node]:
      if dist[node] + 1 < dist[adjNode]: # Check if the (curr_path + 1) is shorter than previously found paths
        dist[adjNode] = dist[node]+1
        queue.append(adjNode)
  
  # Updated shortest distances are stored in the resultant array ‘ans’. Unreachable nodes are marked as -1.
  res = [-1 if d == float('inf') else d for d in dist]
  return res

def shortestPathUnitWeight(edges: List[List[int]], n: int, m: int, src: int) :
  adj = defaultdict(list)
  
  for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
    
  dist = [float('inf')]*n
  dist[src] = 0
  queue = deque([src])
  
  while queue:
    node = queue.popleft()
    
    for adjNode in adj[node]:
      if dist[node]+1 < dist[adjNode]:
        dist[adjNode] = dist[node]+1
        queue.append(adjNode)
  
  res = [-1 if num == float('inf') else num for num in dist]
  return res
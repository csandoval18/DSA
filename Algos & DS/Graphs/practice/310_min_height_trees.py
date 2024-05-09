from collections import defaultdict, deque
from typing import List

# Remember:
# Notice that the problem is looking for min height TREE not DAG, so we can not use 

def findMinHeightTreesBFS(n: int, edges: List[List[int]]) -> List[int]:
  if n == 1:
    return [0]
  if n == 2:
    return [0, 1] # Direct connection between the only two nodes
  
  # Building the graph
  adj = defaultdict(list)
  for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
  
  # Initialize the first layer of leaves
  queue = deque([i for i in range(n) if len(adj[i]) == 1])
  
  # Trimp the leaves until the number of nodes is <= 2
  remaining_nodes = n
  while remaining_nodes > 2:
    leaves_count = len(queue)
    remaining_nodes -= leaves_count
    
    for _ in range(leaves_count):
      leaf = queue.popleft()
      # Each leaf has exactly one neighbor
      neighbor = adj[leaf].pop() # Get and remove the only neighbor
      adj[neighbor].remove(leaf) # Remove leaaf from its neighbor's set
      
      # Check if this neighbor has become a leaf
      if len(adj[neighbor]) == 1:
        queue.append(neighbor)
  
  # The remaining nodes are the roots of the minimum height trees
  return list(queue)

def findMinHeightTreesDFS(n: int, edges: List[List[int]]) -> List[int]:
  if n == 1:
    return [0]
    
  adj = defaultdict(list)
  
  for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
    
  edge_cnt = {}
  queue = deque()
  for src, neighbors in adj.items():
    if len(neighbors) == 1:
      edge_cnt[src] = len(neighbors)
  
  while queue:
    if n <= 2:
      return list(queue)
      
    for node in range(len(queue)):
      node = queue.popleft()
      
      for it in adj[node]:
        edge_cnt[it] -= 1
        if edge_cnt == 1:
          queue.append(it)
  
  # Indegree
  # for node in range(n):
  #   if len(adj[node]) == 1: 
  #     queue.append()
  #     edge_cnt = len(adj[node])

  
  
  
  
# Example usage
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print(findMinHeightTrees(n, edges))  # Output: [3, 4]
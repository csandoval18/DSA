# Kruskal's Algorithm

# Sort all the edges according to weight
from ast import List


edges = [
# wt  u  v
  [1, 1, 4],
  [2, 1, 2],
  [3, 2, 3],
  [3, 2, 4],
  [4, 1, 5],
  [5, 3, 4],
  [7, 2, 6],
  [8, 3, 6],
  [9, 4, 5]
]


class DisjointSet:
  def __init__(self, V: int) -> None:
    self.parent = [i for i in range(V+1)]
    self.size = [1] * (V+1)
    
  def findUltimateParent(self, node: int) -> int: 
    if node == self.parent[node]:
      return node
    
    self.parent[node] = self.findUltimateParent(self.parent[node])
    return self.parent[node]
  
  def unionBySize(self, u: int, v: int) -> None:
    root_u = self.findUltimateParent(u)
    root_v = self.findUltimateParent(v)
    
    if root_u == root_v:
      return 
    
    if self.size[root_u] < self.size[root_v]:
      self.parent[root_u] = self.parent[root_v]
      self.size[root_v] += self.size[root_u]
    else:  
      self.parent[root_v] = root_u
      self.size[root_u] += self.size[root_v]
    

def spanningTree(V: int, adj: List[List[int]]):
  edges = []
  
  # O(V+E)
  # Finding all edges (wt, node, adjNode)
  for node in range(V):
    for adjNode, wt in adj[node]:
      edges.append((wt, node, adjNode))
  edges.sort() # Sort the edges based on weight
  
  ds = DisjointSet(V) # Declare disjoint data structure
  mst_wt = 0 
  
  for wt, u, v in edges:
    if ds.findUltimateParent(u) != ds.findUltimateParent(v): # Check if nodes belong in a different component
      mst_wt += wt
      ds.unionBySize(u, v)
  return mst_wt
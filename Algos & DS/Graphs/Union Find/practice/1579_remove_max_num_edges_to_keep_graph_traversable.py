from collections import defaultdict
from typing import List

class UnionFind:
  def __init__(self, size) -> None:
    self.parent = list(range(size))
    self.size = [1] * size
  
  def find(self, u: int) -> int:
    if self.parent[u] != u:
      self.parent[u] = self.find(self.parent[u])
    return self.parent[u]
  
  def union(self, u: int, v: int) -> bool:
    rootU = self.find(u)
    rootV = self.find(v)
    
    if rootU != rootV:
      if self.size[rootU] > self.size[rootV]:
        self.parent[rootV] = rootU
        self.size[rootU] += self.size[rootV]
      else:
        self.parent[rootU] = rootV
        self.size[rootV] += self.size[rootU]
      return True
    return False

class Solution:
  def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
    alice_union_find = UnionFind(n+1)
    bob_union_find = UnionFind(n+1)
    total_union_find = UnionFind(n+1)
    
    removed_edges = 0
    used_edges = 0
    
    # Process type 3 edges first (common to both Alice and Bob)
    for edge_type, u, v in edges:
      if edge_type == 3:
        if total_union_find.union(u, v):
          alice_union_find.union(u, v)
          bob_union_find.union(u, v)
          used_edges += 1
        else:
          removed_edges += 1

    # Process type 2 edges (Bob only)
    for edge_type, u, v in edges:
      if edge_type == 2:
        if bob_union_find.union(u, v):
          used_edges += 1
        else:
          removed_edges += 1
    
    # Check if both Alice and Bob can fully traverse their graphs
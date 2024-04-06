# Union (u,v)
# 1. Find ultimate parent of u & v, pu, pv
# 2. Find rank of pu, pv
# 3. Connect smaller ranks to longer ranks always

class DisjointSet:
  def __init__(self, n: int) -> None:
    self.rank = [0] * (n+1)
    self.parent = [i for i in range(n+1)]
    self.size = [1]*(n+1)
    
  def findUltimateParent(self, node: int) -> int: 
    if node == self.parent[node]:
      return node
    
    self.parent[node] = self.findUltimateParent(self.parent[node])
    return self.parent[node]
  
  def unionByRank(self, u: int, v: int) -> None: # Path compression
    root_u = self.findUltimateParent(u)
    root_v = self.findUltimateParent(v)
    
    if root_u == root_v:
      return
    
    if self.rank[root_u] < self.rank[root_v]:
      self.parent[root_u] = root_v
    elif self.rank[root_v] < self.rank[root_u]:
      self.parent[root_v] = root_u
    else:
      self.parent[root_v] = root_u
      self.rank[root_u] += 1
  
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
    


ds = DisjointSet(7)
ds.unionByRank(1, 2)
ds.unionByRank(2, 3)
ds.unionByRank(4, 5)
ds.unionByRank(6, 7)
ds.unionByRank(5, 6)
# If 3 and 7 are the same component or not
if ds.findUltimateParent(3) == ds.findUltimateParent(7):
  print("Same")
else:
  print("Not the same")
ds.unionByRank(3, 7)
if ds.findUltimateParent(3) == ds.findUltimateParent(7):
  print("Same")
else:
  print("Not the same")
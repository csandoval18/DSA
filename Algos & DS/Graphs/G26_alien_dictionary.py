from collections import defaultdict, deque
from typing import List

def findOrder(alien_dict: List[str], N: int, K: int) -> List[str]:
  adj = defaultdict(str)
  
  # We are comparing 2 strings
  for i in range(N-1):
    s1 = alien_dict[i]
    s2 = alien_dict[i+1]
    min_len = min(len(s1), len(s2))
    for j in range(min_len):
      if s1[j] != s2[j]:
        adj[s1[j]].append(s2[j])
        break
  
  def topoSort(V: int, adj: List[List[int]]) -> List[int]:
    indegree = [0]*V
    topo = []
    
    for node in range(V):
      for adjNode in adj[node]:
        indegree[adjNode] += 1
    
    queue = deque()
    for node in range(V):
      if indegree[node] == 0:
        queue.append(node)
        
    while queue:
      node = queue.popleft()
      topo.append(node)
      
      for adjNode in adj[node]:
        indegree[adjNode] -= 1
        if indegree[adjNode] == 0:
          queue.append(indegree)
  
    return topo
    
  topo = topoSort(K, adj)
  topo_str = " ".join(topo)
  return topo_str
  
  
# Follow up:
# When is the order not possible?

# 1. When the larger string is above the shorter string, ex:
# Not possible   Possible
# s1 = "abcd"    s1 = "abc"
# s2 = "abc"     s2 = "abcd"

# 2. When there is a cyclic dependency, ex:
# abc
# bat
# ade

# Notice how the 'a' order is not consistant: a -> b -> a
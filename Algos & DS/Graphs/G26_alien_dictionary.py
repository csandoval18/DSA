from collections import deque
from typing import List

def findOrder(alien_dict: List[str], N: int, K: int) -> List[str]:
  adj = [0]*K
  
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
    for 
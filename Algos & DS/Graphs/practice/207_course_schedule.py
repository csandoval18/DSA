from collections import defaultdict, deque
from typing import List


class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    adj = defaultdict(list)
    indegree = [0] * numCourses
    topo_cnt = 0
    
    for u, v in prerequisites:
      adj[u].append(v)
      indegree[u] += 1
    
    q = deque()
    for node in range(numCourses):
      if indegree[node] == 0:
        q.append(node)
    
    while q:
      node = q.popleft()
      topo_cnt += 1
      
      for it in adj[node]:
        indegree[it] -= 1
        if indegree[it] == 0:
          q.append(it)
        
    return topo_cnt == numCourses
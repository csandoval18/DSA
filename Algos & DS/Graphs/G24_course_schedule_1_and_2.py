from collections import defaultdict, deque
from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
  graph = defaultdict(list)
  indegree = [0]*numCourses
  topo_cnt = 0
  
  # for node in range(numCourses):
  #   for adjNode in range(prerequisites[node]):
  for adjNode, node in prerequisites:
    graph[node].append(adjNode)
    indegree[adjNode] += 1
  
  queue = deque()
  for node in range(numCourses):
    if indegree[node] == 0:
      queue.append(node)
  
  while queue:
    node = queue.popleft()
    topo_cnt += 1
    
    for adjNode in prerequisites[node]:
      indegree[adjNode] -= 1
      if indegree[adjNode] == 0:
        queue.append(adjNode)
  
  return topo_cnt == numCourses
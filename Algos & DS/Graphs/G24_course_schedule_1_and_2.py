from collections import defaultdict, deque
from typing import List

def canFinish1(numCourses: int, prerequisites: List[List[int]]) -> bool:
  adj = defaultdict(list)
  indegree = [0]*numCourses
  topo_cnt = 0
  
  # for node in range(numCourses):
  #   for adjNode in range(prerequisites[node]):
  for adjNode, node in prerequisites:
    adj[node].append(adjNode)
    indegree[adjNode] += 1
  
  queue = deque()
  for node in range(numCourses):
    if indegree[node] == 0:
      queue.append(node)
  
  while queue:
    node = queue.popleft()
    topo_cnt += 1
    
    for adjNode in adj[node]:
      indegree[adjNode] -= 1
      if indegree[adjNode] == 0:
        queue.append(adjNode)
  
  return topo_cnt == numCourses
  

def canFinish2(numCourses: int, prerequisites: List[List[int]]) -> bool:
  adj = defaultdict(list)
  indegree = [0]*numCourses
  topo = []
  
  for next_course, prereq in prerequisites:
    adj[prereq].append(next_course)
    indegree[next_course] += 1
  
  queue = deque()
  for course in range(numCourses):
    if indegree[course] == 0:
      queue.append(course)
    
  while queue:
    prereq = queue.popleft()
    topo.append(prereq)
    
    for next_course in adj[prereq]:
      indegree[next_course] -= 1
      if indegree[next_course] == 0:
        queue.append(next_course)
    
  if len(topo) == numCourses:
    return topo
  return []


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
  adj = defaultdict(list)
  indegree = [0]*numCourses
  topo = []
  
  for adjNode, node in prerequisites:
    adj[node].append(adjNode)
    indegree[adjNode] += 1
  
  queue = deque()
  for node in range(numCourses):
    if indegree[node] == 0:
      queue.append(node)
  
  while queue:
    node = queue.popleft()
    topo.append(node)

    for adjNode in adj[node]:
      indegree[adjNode] -= 1
      if indegree[adjNode] == 0:
        queue.append(adjNode)

  if len(topo) == numCourses:
    return topo
  return []
        
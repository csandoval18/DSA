from collections import defaultdict, deque
from typing import List

def topoSort(graph: List[List[int]]) -> List[int]:
  V = len(graph)
  indegree = [0]*V
  topo = []
  
  for node in range(V):
    for it in graph[node]:
      # Remember for topo sort we increase the adjacent node in-degree
      indegree[it] += 1
  
  q = deque()
  for node in range(V):
    if indegree[node] == 0:
      q.append(node)
  
  while q:
    node = q.popleft()
    topo.append(node)
    
    for it in graph[node]:
      indegree[it] -= 1
      if indegree[it] == 0:
        q.append(it)
        
  return topo

def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
  V = len(graph)
  reversed_graph = defaultdict(list)
  indegree = [0]*V
  
  # Reverse the graph and calculate in-degrees
  for u in range(V):
    for v in graph[u]:
      reversed_graph[v].append(u)
      indegree[u] += 1
  
  q = deque([node for node in range(V) if indegree[node] == 0])
  topo = []
  
  # Kahn's algorithm for topological sorting
  while q:
    node = q.popleft()
    topo.append(node)
    
    for it in reversed_graph[node]:
      indegree[it] -= 1
      if indegree[it] == 0:
        q.append(it)
  
  return sorted(topo)
    
  
graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
# Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either of them.
# Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
print(eventualSafeNodes(graph))

































# from typing import List

# def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
#     n = len(graph)
#     state = [0] * n  # 0 = unvisited, 1 = visiting, 2 = safe

#     def dfs(node):
#         if state[node] != 0:
#             return state[node] == 2
        
#         state[node] = 1  # Mark the node as visiting
#         for neighbor in graph[node]:
#             if not dfs(neighbor):  # If any neighbor is not safe, this node is not safe
#                 return False
        
#         state[node] = 2  # Mark the node as safe
#         return True

#     # Find all safe nodes
#     safe_nodes = []
#     for node in range(n):
#         if dfs(node):
#             safe_nodes.append(node)
    
#     return safe_nodes

# Example usage
# graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# print(eventualSafeNodes(graph))  # Output: [2, 4, 5, 6]

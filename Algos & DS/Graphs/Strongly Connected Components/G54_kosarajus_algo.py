# Kosaraju's Algorithm

# Questions Ex:
# 1. Find the number of strongly connected components
# 2. Print the strongly connected components

# 1. Sort all the edges according to finishing time
# 2. Reverse the graph 
# 3. Perform a dfs

from ast import List


def kosaraju(V: int, adj: List[List[int]]) -> int:
  visited = [False]*V
  stack = []
  
  def dfs(node: int, adjList: List[List[int]]) -> None:
    visited[node] = True
    
    for adjNode in adjList[node]:
      if not visited[adjNode]:
        dfs(adjNode, adjList)
    
    stack.append(node)
  
  # Perform first dfs to fill up stack order according to finishing time
  for node in range(V):
    if not visited[node]:
      dfs(node, adj)

  # Reverse every edge direction
  adjReverse = [[] for _ in range(V)]
  for node in range(V):
    for adjNode in adj[node]:
      adjReverse[adjNode].append(node)
  
  visited = [False]*V # Reset visited list
  scc = 0
  
  # Perform second dfs on stack order for reversed adj list to find scc's
  while stack:     
    node = stack.pop()
    
    if not visited[node]:
      scc += 1
      dfs(node)
  return scc
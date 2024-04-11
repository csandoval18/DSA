# time[] =  store the time of dfs traversal starting 1 and incrementing to V vertices
# low[] = min entry point of dfs serach

# Main difference between this problem and the bridges one is that for this one we are removing the node itself,
# not the edge like in the bridge problem so we have to take into account the adjacent/parent node of the removed node

from typing import List

def articulationPoints(V: int, adj: List[List[int]]):
  visited = [False]*V
  time = [0]*V
  low = [0]*V
  mark = [0]*V
  timer = [0]
  
  def dfs(node: int, parent: int):
    visited[node] = True
    time[node] = low[node] = timer[0]
    timer[0] += 1
    child = 0
    
    for it in adj[node]:
      if it == parent:
        continue
      if not visited[it]:
        dfs(it, node)
        low[node] = min(low[node, low[it]])
        if low[it] >= time[node] and parent != -1:
          mark[node] = 1
        child += 1
      else:
        low[node] = min(low[node, time[it]])
    
    if child > 1 and parent == -1:
      mark[node] = 1
  
  for node in range(V):
    if not visited[node]:
      dfs(node, -1)
  
  res = []
  for node in range(V):
    if mark[node] == 1:
      res.append(node)
  
  if len(res) == 0:
    return [-1]
  return res

# The starting node can not be the articulation point that is why we need to check (parent != -1) because if the starting node is removed
# then we would still have one component
# Ex: If we remove 0 then there is still one component

#    0
#    |
#    1
#   / \
#  2   3


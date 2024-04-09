# time[] =  store the time of motion during dfs
# low[] = min of all adj nodes apart frm parent & visited nodes

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
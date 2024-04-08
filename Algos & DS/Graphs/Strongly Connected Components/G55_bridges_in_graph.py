# tm[] = time of insertion
# low[] = min lowerst time insertion of all adj nodes apart from parent

# 1192. Critical Connections in a Network
from ast import List

def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
  adj = [[] for _ in range(n)]
  
  for u, v in connections:
    adj[u].append(v)
    adj[v].append(u)
  
  visited = [False]*n
  time = [0]*n
  low = [0]*n
  bridges = []
  timer = [1]
  
  def dfs(node: int, parent: int):
    visited[node] = True
    time[node] = low[node] = timer[0]
    timer += 1
    
    for adjNode in adj[node]:
      if adjNode == parent:
        continue
      if not visited[adjNode]:
        dfs(adjNode, node)
        low[node] = min(low[node], low[adjNode])
        # Check if the current edge is a bridge
        if low[adjNode] > time[node]:
          bridges.append([node, adjNode])
      else:
        low[node] = min(low[node], low[adjNode])
    
  dfs(0, -1)
  return bridges
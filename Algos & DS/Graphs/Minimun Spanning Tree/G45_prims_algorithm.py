from ast import List
import heapq

def spanningTree(V: int, adj: List[List[int]]) -> List[int]:
  visited = [False]*V
  pq = [(0,0)]
  total_sum = 0
  
  while pq:
    wt, node = heapq.heappop(pq)
    
    if visited[node]:
      continue
      
    visited[node] = True
    total_sum += wt
    
    for adjNode, edW in adj[node]:
      if not visited[adjNode]:
        heapq.heappush(pq, (edW, adjNode))
    
  return total_sum
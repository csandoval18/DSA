from collections import defaultdict
from heapq import heappop, heappush
from typing import List, Tuple


class Solution:
  def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
    adj = [[] for _ in range(n)]
    INF = int(2 * 1e9)
    weights = defaultdict(lambda: defaultdict(int))
    
    for u, v, w in edges:
      adj[u].append((v, w))
      adj[v].append((u, w))
      
      if w == -1:
        weights[u][v] = weights[v][u] = 1
        
    def dijkstra(source: int):
      parents = [-1 for _ in range(n)]
      pq = [(0, source)]
      dist = [INF for _ in range(n)]
      confirmed = [False for _ in range(n)]
      
      while pq:
        uw, u = heappop(pq)
        
        if confirmed[u]:
          continue
        dist[u] = uw
        confirmed[u] = True
        
        for v, vw in adj[u]:
          if vw == -1:
            vw = weights[u][v]
            
          nc = uw + vw
          if nc < dist[v]:
            parents[v] = u
            dist[v] = nc
            heappush(pq, (nc, v)) 
            
      paths = []
      now = destination
      
      while now != source:
        nxt = parents[now]
        if weights[nxt][now] >= 1 and weights[nxt][now] < INF:
          paths.append((nxt, now))
        now = nxt
      return (dist[destination], paths)
      
    # def form_answer() -> List[List[int]]:
    #   ans = []
    #   for u, v, w in edges:
    #     if w == -1:
    #       ans.append((u, v, weights[u][v]))
    #     else:
    #       ans.append((u, v, w))
    #   return ans
      
    min_cost_now, min_cost_path = dijkstra()
    while min_cost_now != target:
      if min_cost_now > target or len(min_cost_path) == 0:
        return []
        
      u, v = min_cost_path[0]
      diff = target - min_cost_now
      weights[u][v] = weights[v][u] = weights[v][u] + diff
      min_cost_path_s = set(min_cost_path)
      
      for u, v, w in edges:
        not_exist = (u, v) not in min_cost_path_s and (v, u) not in min_cost_path_s
        if w == -1 and not_exist:
          weights[u][v] = weights[v][u] = INF
      min_cost_now, min_cost_path = dijkstra()
    
    res = []
    for u, v, w in edges:
      if w == -1:
        res.append((u, v, weights[u][v]))
      else:
        res.append((u, v, w))
    return res
from typing import List


class Solution:
  def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
    adj = [[] for _ in range(n)]
          inf = int(2 * 1e9)
          weights = defaultdict(lambda: defaultdict(int))
          for u, v, w in edges:
              adj[u].append((v, w))
              adj[v].append((u, w))
              if w == -1:
                  weights[u][v] = weights[v][u] = 1
          def dijkstra() -> (int, List[int]):
              parents = [-1 for _ in range(n)]
              min_heap = [(0, source)]
              min_costs = [inf for _ in range(n)]
              confirmed = [False for _ in range(n)]
              while len(min_heap):
                  cost, cur = heappop(min_heap)
                  if confirmed[cur]: continue
                  min_costs[cur] = cost
                  confirmed[cur] = True
                  for nei, weight in adj[cur]:
                      if weight == -1:
                          weight = weights[cur][nei]
                      nei_cost = cost + weight
                      if nei_cost < min_costs[nei]:
                          parents[nei] = cur
                          min_costs[nei] = nei_cost
                          heappush(min_heap, (nei_cost, nei)) 
              paths = []
              now = destination
              while now != source:
                  nxt = parents[now]
                  if weights[nxt][now] >= 1 and weights[nxt][now] < inf:
                      paths.append((nxt, now))
                  now = nxt
              return (min_costs[destination], paths)
          def form_answer() -> List[List[int]]:
              ans = []
              for u, v, w in edges:
                  if w == -1:
                      ans.append((u, v, weights[u][v]))
                  else:
                      ans.append((u, v, w))
              return ans
          min_cost_now, min_cost_path = dijkstra()
          while min_cost_now != target:
              if min_cost_now > target or len(min_cost_path) == 0: return []
              u, v = min_cost_path[0]
              diff = target - min_cost_now
              weights[u][v] = weights[v][u] = weights[v][u] + diff
              min_cost_path_s = set(min_cost_path)
              for u, v, w in edges:
                  not_exist = (u, v) not in min_cost_path_s and (v, u) not in min_cost_path_s
                  if w == -1 and not_exist:
                      weights[u][v] = weights[v][u] = inf
              min_cost_now, min_cost_path = dijkstra()
          return form_answer()
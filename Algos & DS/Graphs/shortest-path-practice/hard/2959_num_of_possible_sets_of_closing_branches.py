from heapq import heappop, heappush
import itertools
from typing import List


class Solution:
  def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
    def check(subset: List[int]):
      dist = [[float('inf')] * n for _ in range(n)]
      for i in range(n):
        dist[i][i] = 0
      for u, v, w in roads:
        if u in subset and v in subset:
          dist[u][v] = min(dist[u][v], w)
          dist[v][u] = min(dist[v][u], w)
      for k in subset:
        for i in subset:
          for j in subset:
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
      for i in subset:
        for j in subset:
          if dist[i][j] > maxDistance:
            return False
      return True
    
    ans = 0
    for r in range(n + 1):
        for subset in itertools.combinations(range(n), r):
            if check(subset, n, maxDistance, roads):
                ans += 1
    return ans


n = 3
maxDistance = 5
roads = [[0,1,2],[1,2,10],[0,2,10]]
# Output: 5
# Explanation: The possible sets of closing branches are:
# - The set [2], after closing, active branches are [0,1] and they are 
#   reachable to each other within distance 2.
# - The set [0,1], after closing, the active branch is [2].
# - The set [1,2], after closing, the active branch is [0].
# - The set [0,2], after closing, the active branch is [1].
# - The set [0,1,2], after closing, there are no active branches.
# It can be proven, that there are only 5 possible sets of closing branches.
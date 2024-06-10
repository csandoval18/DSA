from collections import defaultdict
import heapq
from typing import List


# In solving the "787. Cheapest Flights Within K Stops" problem, a separate distance array is not strictly
# necessary because the priority queue inherently manages the exploration of minimum cost paths
# efficiently. The priority queue ensures that we always process the node with the smallest current cost
# first, effectively minimizing the path cost dynamically. By keeping track of the remaining stops, the
# algorithm limits unnecessary revisits and redundant calculations. This approach leverages the 
# properties of the priority queue to find the shortest path within the allowed stops, thus simplifying 
# the implementation while maintaining efficiency.

class Solution:
  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    adj = [[] for _ in range(n)]

    for u, v, w in flights:
      adj[u].append((v, w))

    dist = [float('inf')]*n # changed
    dist[src] = 0
    pq = [(0, src, k+1)]

    while pq:
      cost, u, stops = heapq.heappop(pq)
      if u == dst:
        return cost
          
      if stops == 0:
        continue
      for v, w in adj[u]:
        if cost + w < dist[v]:
          dist[v] = cost + w
          heapq.heappush(pq, (dist[v], v, stops-1))

    return -1

import heapq

class Solution1:
  def findCheapestPrice(self, n, flights, src, dst, k):
    print("hi")
    graph = [[] for _ in range(n)]

    for flight in flights:
      u, v, w = flight
      graph[u].append((v, w))

    return self.dijkstra(graph, src, dst, k)

  def dijkstra(self, graph, src, dst, k):
      INF = float('inf')
      dist = [[INF] * (k + 2) for _ in range(len(graph))]
      minHeap = [(0, src, k + 1)]

      dist[src][k + 1] = 0

      while minHeap:
        d, u, stops = heapq.heappop(minHeap)
        if u == dst:
          return d
        if stops == 0:
            continue
        for v, w in graph[u]:
          if d + w < dist[v][stops - 1]:
            dist[v][stops - 1] = d + w
            heapq.heappush(minHeap, (dist[v][stops - 1], v, stops - 1))

      return -1

          
n = 5
# flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
# flights = [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]]
flights = [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]]
src = 0 # Source node
dst = 2 # Destination node
k = 2 # Number of stops allowed (count of nodes allowed between source and destination)
# Output: 700

s = Solution()
print(s.findCheapestPrice(n, flights, src, dst, k))
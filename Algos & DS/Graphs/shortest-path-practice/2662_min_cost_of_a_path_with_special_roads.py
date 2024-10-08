from collections import defaultdict
import heapq
from typing import List

# Given start: where start = [startX, startY] represents your initial position in a 2D space.
# Given target: where target = [targetX, targetY] represent your target position (targetX, targetY)

# The cost of going from position (x1, y1) to any other position in the space (x2, y2) is 
# | x2 - x1 | + | y2 - y1 | 

# There are also some special roads. You are given a 2D array specialRoads where 
# specialRoads[i] = [x1, y1, x2, y2, cost] indicates that the ith special road goes in *(one direction) from (x1, y1) to (x2, y2)
# with a cost equal to cost. You can use each special road any number of times.

# Return the min cost reqired to go from (startX, startY) to (targetX, targetY)

class Solution:
  def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
    def manhattan(p1: List[int], p2: List[int]): # Function to calculate the Manhatan distance between two points
      return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    # Collect all unique points including start, target, and all special roads
    points = [start, target] + [[road[0], road[1]] for road in specialRoads] 
    + [[road[2], road[3]] for road in specialRoads]
    
    points = list(set(map(tuple, points))) # Remove duplicates and convert to tuple for hashing
    point_to_idx = {point: i for i, point in enumerate(points)}
    
    # Number of unique points
    n = len(points)
    adj = {i: [] for i in range(n)} # Initialize adjacency list
    
    for i, (x1, y1) in enumerate(points):
      for j, (x2, y2) in enumerate(points):
        if i != j:
          adj[i].append((j, manhattan((x1,  y1), (x2, y2))))
    
    # Add edges for special roads with their specific costs
    for x1, y1, x2, y2, cost in specialRoads:
      u = point_to_idx[(x1, y1)]
      v = point_to_idx[(x2, y2)]
      adj[u].append((v, cost))
    
    start = point_to_idx[tuple(start)]
    target = point_to_idx[tuple(target)]
    
    pq = [(0, start)] # (cost, node)
    
    dist = [float('inf')] * n
    dist[start] = 0
    
    while pq:
      ud, u = heapq.heappop(pq)
      
      if u == target:
        return ud
      
      if ud > dist[u]:
        continue
        
      for v, vd in adj[u]:
        nd = ud + vd
        
        if nd < dist[v]:
          dist[v] = nd
          heapq.heappush(pq, (v, nd))
    return -1


class SolutionFaster:
  def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
    return self.dijkstra(specialRoads, *start, *target)

  def dijkstra(self, specialRoads: List[List[int]], srcX: int, srcY: int, dstX: int, dstY: int) -> int:
    n = len(specialRoads)
    dist = [float('inf')] * n # dist[i] := the minimum distance of (srcX, srcY) to specialRoads[i](x2, y2)
    pq = []  # (d, u),(d, u), where u := the i-th specialRoads

    for u, (x1, y1, _, _, cost) in enumerate(specialRoads): # (srcX, srcY) -> (x1, y1) to cost -> (x2, y2)
      d = abs(x1 - srcX) + abs(y1 - srcY) + cost
      dist[u] = d
      heapq.heappush(pq, (dist[u], u))

    while pq:
      d, u = heapq.heappop(pq)
      
      if d > dist[u]:
        continue
      
      _, _, ux2, uy2, _ = specialRoads[u]
      
      for v in range(n):
        if v == u:
          continue
        
        vx1, vy1, _, _, vcost = specialRoads[v]
        newDist = d + abs(vx1 - ux2) + abs(vy1 - uy2) + vcost # (ux2, uy2) -> (vx1, vy1) to vcost -> (vx2, vy2)
        
        if newDist < dist[v]:
          dist[v] = newDist
          heapq.heappush(pq, (dist[v], v))

    ans = abs(dstX - srcX) + abs(dstY - srcY)
    for u in range(n):
      _, _, x2, y2, _ = specialRoads[u]
      ans = min(ans, dist[u] + abs(dstX - x2) + abs(dstY - y2)) # (srcX, srcY) -> (x2, y2) -> (dstX, dstY).

    return ans
            
    


start = [1, 1]
target = [4, 5]
specialRoads = [[1,2,3,3,2], [3,4,4,5,1]]
s = Solution()
print(s.minimumCost(start, target, specialRoads))
# Output: 5
from collections import defaultdict
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
    def manhattan(p1: List[int], p2: List[int]):
      return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    points = [start, target] + [[road[0], road[1]] for road in specialRoads] + [[road[2], road[3]] for road in specialRoads]
    points = list(set(map(tuple, points))) # REmove duplicates and convert to tuple for hashing
    point_to_idx = {point: i for i, point in enumerate(points)}
    
    n = len(points)
    adj = {i: [] for i in range(n)}
    
    for i, (x1, y1) in enumerate(points):
      for j, (x2, y2) in enumerate(points):
        if i != j:
          adj[i]
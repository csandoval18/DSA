# Floyd Warshall's Algorithm

# This algorithm varies from the previous shortest path primarily because it finds the multi source shortest path
# Basically this brute forces the paths of all paths for every kth node and stores the shortest (min) path in a 2d array since it is
# a dynamic programming algorithm

# This is best used on graphs with small amounts of vertices

from typing import List

def shortest_distance(matrix: List[List[int]]) -> List[int]:
  n = len(matrix)
  
  # Change -1's in matrix to inf, -1's symbolize no edge from source to dest node
  for i in range(n):
    for j in range(n):
      if matrix[i][j] == -1:
        matrix[i][j] = float('inf')
      if i == j: # When i and j are equal we are comparing the distance to travel between the same node wich is 0. See matrix 1
        matrix[i][j] = 0
      
  for k in range(n):
    for i in range(n):
      for j in range(n):
        # Compare the current value matrix[i][j] to the kth node path min(matrix[i][k] + min[k][j])
        matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
  
  # Change inf's back to -1
  for i in range(n):
    for j in range(n):
      if matrix[i][j] == float('inf'):
        matrix[i][j] = -1


# Matrix 1  
#    0 1 2 3
# 0 [0 1 1 1]
# 1 [1 0 1 1]
# 2 [1 1 0 1]
# 3 [1 1 1 0]

# Ignore the 1's. In the actual problem there will be edge weights between the nodes. Notice how the diagonal line of 0s when i = j.
# This just symbolizes that there is no cost to travel to the same node.



# Example:
# 1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

# This problems shows how we would create the adjacency matrix to handle the algirthm

class Solution:
  def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int: 
    dist = [[float('inf')]*n for _ in range(n)] # Declare adjacency matrix keeping track of weights between nodes
    
    for u in range(n): # Set distance of a node to travel to itself to 0
      dist[u][u] = 0
    
    for u, v, w in edges:
      dist[u][v] = w
      dist[v][u] = w
    
    for k in range(n):
      for u in range(n):
        for v in range(n):
          dist[u][v] = min(dist[u][v], dist[u][v] + dist[u][k] + dist[k][v]) # Find shortest paths
    
    # Find the city with the smallest number of cities that are reachable through some path and
    # whose distance is at most distanceThreshold. Return the city with the greatest number if there are multiple cities.
    min_v_cnt = float('inf')
    res_city = -1
    
    # Traverse through dist matrix
    for u in range(n):
      v_cnt = 0
      
      for v in range(n):
        # Find count of paths that are <= distance threshold and make sure the node path is not to itself
        if dist[u][v] <= distanceThreshold and u != v:
          v_cnt += 1
          
      # Check current reachable cities count is < the stored min reachable cities found so far OR 
      # if the current reachable cities count is == to the stored min reachable cities count then we
      # need to check if the current node is bigger than the current responce city. If condiditons are met
      # update the min_v_cnt and response city.
      if v_cnt < min_v_cnt or (v_cnt == min_v_cnt and u > res_city):
        min_v_cnt = v_cnt
        res_city = u
          
    return res_city
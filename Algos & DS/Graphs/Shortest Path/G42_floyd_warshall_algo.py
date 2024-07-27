# Floyd Warshall's Algorithm

# This algorithm varies from the previous shortest path primarily because it finds the multi source shortest path
# Basically this brute forces the paths of all paths for every kth node and stores the shortest (min) path in a 2d array since it is
# a dynamic programming algorithm

# This is best used on graphs with small amounts of vertices

from typing import List

def shortest_distance(matrix: List[List[int]]) -> List[int]:
  n = len(matrix)
  
  # Change -1's in matrix to inf
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
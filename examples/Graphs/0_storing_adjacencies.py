from typing import List

adjacencies = [
  [1,2]
  [1,3]
  [2,4]
  [3,4]
  [3,5]
  [4,5]
]

# n nodes
n = 5
# m edges
m = 6

# Adjacency Matrix
#   0 1 2 3 4 5
# 0 0 0 0 0 0 0
# 1 0 0 1 1 0 0
# 2 0 0 0 0 1 0
# 3 0 0 0 0 1 1
# 4 0 0 0 0 0 1
# 5 0 0 0 0 0 0

def adjacencyMatrix(n: int, m: int, adjacencies: List[List[int]]):
  adj = [[-1 in range(m)] for _ in range(n)]
  
  # m = vertices count
  for i in range(m):
    adj[adjacencies[i][0]][adjacencies[i][1]] = 1
  
  return 0
  
# Adjacency list


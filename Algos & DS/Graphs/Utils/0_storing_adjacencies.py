from typing import List

# To keep track of adjacencies we can use either a 2d array or a list
# The list should be the method to use since it saves space complexity

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

def adjacencyMatrix(n: int, m: int, edges: List[List[int]]):
  adj = [[-1 in range(m)] for _ in range(n)]
  
  # m = vertices count
  for i in range(m):
    adj[edges[i][0]][edges[i][1]] = 1
  
  return 0
  
# Undirected graph (both edges can be traversed from each node)
def adjacencyDict(n: int, edges: List[List[int]]):
  adj = [[] for _ in range(n)]
  
  for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)
  
# Directed graph (can only reach the other node from starting node)
def adjacencyDict(n: int, edges: List[List[int]]):
  adj = [[] for _ in range(n)]
  
  for u, v in edges:
    adj[u].append(v)
  
# Adjacency list
# 0 [1,2]
# 1 [3]
# 2 [4]
# 3 [1,4]
# 4 [2,3]
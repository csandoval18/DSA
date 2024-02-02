# M – Coloring Problem
# Problem Statement: Given an undirected graph and a number m, determine if the graph can be 
# colored with at most m colors such that no two adjacent vertices of the graph are colored with the same color.

# Example 1:
# Input: 
# N  4 = nodes
# M = 3
# E = 5
# Edges[] = {
#   (0, 1),
#   (1, 2),
#   (2, 3),
#   (3, 0),
#   (0, 2)
# }

# Output: 1

# Explanation: It is possible to colour the given graph using 3 colours.

# Example 2:

# Input: 
# Nodes => N = 3
# Colors => M = 2
# Edges => E = 3
# Edges[] = {
#   (0, 1),
#   (1, 2),
#   (0, 2)
# }

# Output: 0

def m_coloring(graph, n, m):
  def isSafe(node, color, graph, n, col):
    for i in range(n):
      if i != node and graph[i][node] == 1 and color[i] == col:
        return False
    return True
  
  def backtrack(node, color, m, n, graph):
    if node == n:
      return True
      
    for i in range(1, m+1): 
      if isSafe(node, color, graph, n, i):
        color[node] = i
        if backtrack(node+1, color, m, n, graph):
          return True
        color[node] = 0
        
    return False
  
  color = [0] * n
  if backtrack(0, color, m, n, graph):
      return True
  return False
  
  
n = 4
m = 3
graph = [[0 for i in range(101)] for j in range(101)]

# Edges are (0, 1), (1, 2), (2, 3), (3, 0), (0, 2)
graph[0][1] = 1
graph[1][0] = 1
graph[1][2] = 1
graph[2][1] = 1
graph[2][3] = 1
graph[3][2] = 1
graph[3][0] = 1
graph[0][3] = 1
graph[0][2] = 1
graph[2][0] = 1
print(1 if m_coloring(graph, m, n) else 0)

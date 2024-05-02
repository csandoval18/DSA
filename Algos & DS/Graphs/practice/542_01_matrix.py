from collections import deque
from typing import List

def updateMatrixAttempt(mat: List[List[int]]) -> List[List[int]]:
  n = len(mat)
  m = len(mat[0])
  res = [[0]*m for _ in range(n)]
  
  
  def bfs(i: int, j: int):
    dist_to_zero = 0
    queue = deque()
    queue.append((i, j))
    
    while queue:
      x, y = queue.popleft()
      
      for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
        nx, ny = dx + x, dy + y
        
        if 0 <= nx < n and 0 <= ny < m:
          if mat[nx][ny] == 0:
            return dist_to_zero
          else:
            queue.append((nx, ny))
            dist_to_zero += 1
            
  for i in range(n):
    for j in range(n):
      if mat[i][j] == 1:
        res[i][j] = bfs(i, j)
  
  return res
      
def updateMatrixAttempt(mat: List[List[int]]) -> List[List[int]]:
  n, m = len(mat), len(mat[0])
  queue = deque()
  dist = [[float('inf')] * m for _ in range(n)] 
  
  for i in range(n):
    for j in range(m):
      if mat[i][j] == 0:
        queue.append((i, j))
        dist[i][j] = 0
  
  while queue:
    x, y = queue.popleft()
    
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
      nx, ny = dx + x, dy + y
      
      if 0 <= nx < n and 0 <= ny < m:
        # Only if we find a shorter path to a cell, we add it to queue
        if dist[nx][ny] > dist[x][y] + 1:
          dist[nx][ny] = dist[x][y] + 1
          queue.append((nx, ny))
  return dist
  
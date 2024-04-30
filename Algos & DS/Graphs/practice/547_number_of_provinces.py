from collections import deque
from typing import List

# Attempt using island search in matrix, but it doesn't work. We can thing of the matrix as a adj list
def findCircleNum(isConnected: List[List[int]]) -> int:
  n = len(isConnected)
  provinces = 0
  
  def bfs(x: int, y: int):
    isConnected[i][j] = 0
    queue = deque()
    queue.append((x, y))
    
    while queue:
      x, y = queue.popleft()
      
      for dx, dy in [(-1,0), (1,0), (0,1), (0,-1)]:
        nx, ny = dx + x, dy + y
        
        if 0 <= nx < n and 0 <= ny < n and isConnected[nx][ny] == 1:
          isConnected[nx][ny] = 0
          queue.append((nx, ny))
  
  for i in range(n):
    for j in range(n):
      if isConnected[i][j] == 1:
        cnt += 1
        bfs(i, j)
  
  return cnt

# Solution
def findCircleNum(isConnected: List[List[int]]) -> int:
  n = len(isConnected)
  visited = [False]*n
  provinces = 0
  
  def bfs(node: int):
    queue = deque([start])
    
    while queue:
      node = queue.popleft()
      
      for it in range(n):
        if isConnected[node][it] 
    
  
  
          

isConnected = [
#  0 1 2 
  [1,1,0], # 0 
  [1,1,0], # 1 
  [0,0,1]  # 2
]
# Output: 2

isConnected = [
  [1,0,0,1],
  [0,1,1,0],
  [0,1,1,1],
  [1,0,1,1]
]

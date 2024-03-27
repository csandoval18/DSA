from collections import deque
from typing import List

# BFS solution using visited matrix
def floodFillBFS(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
  n, m = len(image), len(image[0])
  visited = [[False]*m for _ in range(n)]
  starting_color = image[sr][sc]
  queue = deque()
  queue.append((sr, sc))
  image[sr][sc] = color
  
  while queue:
    x, y = queue.popleft()
    
    delta_matrix = [(1,0),(-1,0),(0,1),(0,-1)]
    for dx, dy in delta_matrix:
      nx = x + dx
      ny = y + dy
      
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and image[nx][ny] == starting_color:
        image[nx][ny] = color
        queue.append((nx, ny))
    
  return image

image = [
  [1,1,1],
  [1,1,0],
  [1,0,1]
] 
sr = 1 
sc = 1 
color = 2
print(floodFillBFS(image, sr, sc, color))


# This version without the visited array does not work for the test case with all the 0s
# Memory limit is exceeded 
def floodFill2(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
  n, m = len(image), len(image[0])
  scolor = image[sr][sc]
  queue = deque()
  
  queue.append((sr, sc))
  image[sr][sc] = color
  
  while queue:
    x, y = queue.popleft()
    
    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
      nx = x + dx
      ny = y + dy
    
      if 0 <= nx < n and 0 <= ny < m and image[nx][ny] == scolor:
        image[nx][ny] = color
        queue.append((nx, ny))
  
  return image

image = [[0,0,0],[0,0,0]]
sr = 0 
sc = 0
color = 0
# print(floodFill2(image, sr, sc, color))


def floodFillDFS(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
  n, m = len(image), len(image[0])
  scolor = image[sr][sc]
  visited = [[False]*m for _ in range(n)]
  image[sr][sc] = color
  
  def dfs(x: int, y: int):
    visited[x][y] = True
    
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
      nx = x + dx
      ny = y + dy
      
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and image[nx][ny] == scolor:
        image[nx][ny] = color
        dfs(nx, ny)

  dfs(sr, sc)
  return image
    
image = [
  [1,1,1],
  [1,1,0],
  [1,0,1]
] 

  
sr = 1 
sc = 1 
color = 2
print(floodFillDFS(image, sr, sc, color))
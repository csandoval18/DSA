from collections import deque
from typing import List

# TC: O(N^2)
def numIslands(matrix: List[List[int]],  n: int, m: int) -> int:
  n, m = len(matrix), len(matrix[0])
  visited = [[False]*m for _ in range(n)]
  island_count = 0
  
  def bfs(row: int, col: int):
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True
    
    while queue:
      r, c = queue.popleft()
      
      # Traverse in the neighbours and mark them if its a land cell
      # Delta row and delta column shortcut for traversing all adjacent cells (including diagonal)
      for dr in range(-1, 2): # -1 <= 1
        for dc in range(-1, 2): # -1 <= 1
          nr = r + dr
          nc = c + dc
          
          if 0 < nr <= n and 0 < nc <= m and matrix[nr][nc] == '1' and not visited[nr][nc]:
            visited[nr][nc] = True
            queue.push((nr, nc))
  
  for i in range(n):
    for j in range(m):
      if not visited[i][j]:
        island_count += 1
        bfs(i, j)
  
  return island_count
      
  
from collections import deque
from typing import List

# Using DFS
def solve(board: List[List[str]]) -> None:
  n, m = len(board), len(board[0])
  
  
  def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or board[x][y] != 'O':
      return
    
    board[x][y] = 'E' # Mark as 'E' to indicate this is not flippable
    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)
    
  # Start DFS from 'O's on the boundary.
  for i in range(n):
    dfs(i, 0)
    dfs(i, m-1)
  
  for i in range(n):
    for j in range(m):
      if board[i][j] == 'O':
        board[i][j] = 'X'
      elif board[i][j] == 'E':
        board[i][j] = 'O' # Restore the original 'O'
        

def solveBFS(board: List[List[str]]) -> None: 
  if not board:
    return

  n, m = len(board), len(board[0])

  # Define the directions to explore
  directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

  # Start BFS from boundary 'O's and mark connected 'O's as not-flippable
  def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
      curr_x, curr_y = queue.popleft()
      
      if 0 <= curr_x < n and 0 <= curr_y < m and board[curr_x][curr_y] == 'O':
        board[curr_x][curr_y] = 'E'  # Mark as not-flippable
        for dx, dy in directions:
          nx, ny = curr_x + dx, curr_y + dy
          queue.append((nx, ny))

  # Start BFS from 'O's on the boundary
  for i in range(n):
    bfs(i, 0)
    bfs(i, m - 1)
  for j in range(m):
    bfs(0, j)
    bfs(n - 1, j)

  # Flip all 'O's to 'X' except those marked as not-flippable ('E')
  for i in range(n):
    for j in range(m):
      if board[i][j] == 'O':
        board[i][j] = 'X'
      elif board[i][j] == 'E':
        board[i][j] = 'O'  # Restore the original 'O' 


def striverSol(board: List[List[str]]) -> None:
  n, m = len(board), len(board[0])
  visited = [[False]*m for _ in range(n)]
  
  def dfs(x: int, y: int):
    visited[i][j] = True
    
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
      nx, ny = dx + x, dy + y
      
      if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'O' and not visited[nx][ny]:
        dfs(nx, ny)
        
  
  for j in range(m):
    # First row
    if not visited[0][j] and board[0][j] == 'O': 
      dfs(0, j)
    
    # Last row
    if not visited[n-1][j] and board[n-1][j] == "O":
      dfs(n-1, j)
    
  for i in range(n):
    # First col
    if not visited[i][0] and board[i][0] == 'O':
      dfs(i, 0)

    # Last col
    if not visited[i][m-1]  and board[i][m-1] == 'O':
      dfs(i, m-1)

  for i in range(n):
    for j in range(m):
      if not visited[i][j] and board[i][j] == 'O':
        board[i][j] = 'X'
  
  return board
    
      
      
  
  
# Example usage
board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
         
solve(board)
for row in board:
  print(row)
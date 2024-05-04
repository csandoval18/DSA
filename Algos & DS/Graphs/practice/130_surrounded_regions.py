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
  
# Example usage
board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
solve(board)
for row in board:
  print(row)
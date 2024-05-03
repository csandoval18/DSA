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
  
  
# Example usage
board = [["X","X","X","X"],
         ["X","O","O","X"],
         ["X","X","O","X"],
         ["X","O","X","X"]]
solve(board)
for row in board:
  print(row)
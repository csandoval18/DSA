from typing import List

def solveNQueens(n: int) -> List[List[str]]:
  def isSafe(row: int, col: int, board: List[str]):
    # Check top left element for Q
    duprow = row
    dupcol = col
    while row >= 0 and col >= 0:
      if board[row][col] == 'Q':
        return False
      row -= 1
      col -= 1
    
    # Check left element for Q
    col = dupcol
    row = duprow
    while col >= 0:
      if board[row][col] == 'Q':
        return False
      col -= 1
      
    #Check bottom left element for Q
    col = dupcol
    row = duprow
    while row < n and col >= 0:
      if board[row][col] == 'Q':
        return False
      row += 1
      col -= 1
      
    # No 'Q's found, so placement is valid at row and col indexes
    return True

  def backtrack(col: List[str], board: List[str]):
    if col == n:
      print("board:", board)
      res.append(board[:])
      return 
    
    for row in range(n):
      if isSafe(row, col, board):
        # This is just replacing the row col position with Q, we need to use slicing since strings are immutable in python
        # Otherwise with an immutable string => board[row][col] = 'Q'
        board[row] = board[row][:col] + 'Q' + board[row][col+1:]
        backtrack(col+1, board)
        board[row] = board[row][:col] + '.' + board[row][col+1:] 
  
  res = []
  board = ['.' * n for _ in range(n)]
  backtrack(0, board)
  return res


n = 4
ans = solveNQueens(n)
for i in range(len(ans)):
  print(f"Arrangement {i+1}")
  for j in range(len(ans[0])):
    print(ans[i][j])
  print()
# 37. Sudoku Solver
# One valid solution only
# [
#   ["...."]
#   ["...."]
#   ["...."]
#   ["...."]
# ]

from typing import List


def solveSudoku(board: List[List[str]]) -> None:
  n = len(board)
  
  def isValid(board: List[List[str]], row: int, col: int, possibleChar: str) -> bool:
    for i in range(9):
      if board[i][col] == possibleChar:
        return False
      if board[row][i] == possibleChar:
        return False
      if board[3 * (row//3)+ i // 3][3 * (col // 3) + i%3] == possibleChar:
        return False
    return True
        

  def backtrack(board: List[List[str]]) -> None:
    for i in range(n):
      for j in range(len(board[0])):
        
        if board[i][j] == '.': # if board cell empty
          for possibleChar in "123456789": # Try out every number from (1-9) as an input
            if isValid(board, i, j, possibleChar):
              board[i][j] = possibleChar
              if backtrack(board):
                return True
              else:
                board[i][j] = "."
          return False
    return True
  
  return backtrack(board)
    
    
  
board = [
    ["9", "5", "7", ".", "1", "3", ".", "8", "4"],
    ["4", "8", "3", ".", "5", "7", "1", ".", "6"],
    [".", "1", "2", ".", "4", "9", "5", "3", "7"],
    ["1", "7", ".", "3", ".", "4", "9", ".", "2"],
    ["5", ".", "4", "9", "7", ".", "3", "6", "."],
    ["3", ".", "9", "5", ".", "8", "7", ".", "1"],
    ["8", "4", "5", "7", "9", ".", "6", "1", "3"],
    [".", "9", "1", ".", "3", "6", ".", "7", "5"],
    ["7", ".", "6", "1", "8", "5", "4", ".", "9"],
]
solveSudoku(board)
for i in range(9):
  for j in range(9):
    print(board[i][j], end=" ")
  print()
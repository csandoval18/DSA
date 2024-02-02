from typing import List

def existAttempt(board: List[List[str]], word: str) -> bool:
  n = len(board)
  m = len(board[0])
  res = False

  def backtrack(idx: int, row, col) -> bool:
    print("row:", row)
    print("col:", col)
    print(idx)
    if idx == len(word):
      return True
    
    # check up
    if row > 0 and board[row-1][col] == word[idx]:
      row -= 1
    # check left 
    elif col > 0 and board[row][col-1] == word[idx]:
      col -= 1
    # check right
    elif col < m-1 and board[row][col+1] == word[idx]:
      col += 1
    # check bottom
    elif row < n-1 and board[row+1][col] == word[idx]:
      row += 1
    else:
      col = col
      row = row
      
    ans = backtrack(idx+1, row, col)
    if ans == True: 
      return True
      
    return False
      
        
  for i in range(n):
    for j in range(m):
      if board[i][j] == word[0]:
        res = backtrack(1, i, j) 
  
  return res
  

def exist(board, word):
  n = len(board)
  m = len(board[0])
  
  def backtrack(row, col, idx): 
    if idx == len(word):
      return True
    
    if 0 <= row < n and 0 <= col < m and board[row][col] == word[idx]:
      # Mark the cell as visited
      tmp = board[row][col]
      board[row][col] = '#'
      
      # Explore neighbor cells
      if (
        backtrack(row+1, col, idx+1) or  
        backtrack(row-1, col, idx+1) or
        backtrack(row, col+1, idx+1) or
        backtrack(row, col-1, idx+1) 
      ):
        return True
        
      # Backtrack by restoring the cell to its original value
      board[row][col] = tmp
    
    return False

  for i in range(n): 
    for j in range(m):
      if backtrack(i, j, 0):
        return True
  return False
      
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCB"
print(exist(board, word))

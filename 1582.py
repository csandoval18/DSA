# Special Positions in a Binary Matrix

# A position (i, j) is called special if mat[i][j] == 1 and all other 
# elements in row i and column j are 0. (rows and cols are 0-indexed)

# BF
def numSpecial(mat: [[int]]) -> int:
  n = len(mat)
  m = len(mat[0])
  res = 0
  
  for i in range(n):
    for j in range(m):
      if mat[i][j] == 1:
        if isSpecialRowCol(mat, i, j, n, m):
          res += 1
  return res
      
def isSpecialRowCol(mat:[[int]], a, b, n, m) -> int:
  for i in range(n):
    if i == a:
      continue
    if mat[i][b] != 0: 
      return False
  for j in range(m):
    if j == b:
      continue
    if mat[a][j] != 0:
      return False
      
  return True

# mat = [[1,0,0],[0,0,1],[1,0,0]]
mat = [[1,0,0],[0,1,0],[0,0,1]]
print(numSpecial(mat))

# [1,0,0]
# [0,0,1]
# [1,0,0]

# Optimize Attempt

# So I noticed that I am rechecking a lot of the the rows and cols for each cell for example I 
# could reuse the check col of mat[0][0] and mat[2][0] since I already checked it in the mat[0][0]
# I am thinking of using 2 arrays for cols and rows that keep track if the row or col contain a 1s

def numSpecial(mat: [[int]]) -> int:
  n = len(mat)
  m = len(mat[0])
  rows = []
  cols = []
    
  for i in range(n):
    if mat[i][j] == 1:
      
  
  for j in range(m):
  
  
  
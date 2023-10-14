# 73. Set Matrix Zeroes

# If a cell has the value 0, then convert that cell's entire row and column values into 0s
# We will convert 1s to -1s to avoid removing other cases with 0s later in a column or row

# Brute Force

def setZeroesBF(matrix):
  n = len(matrix)
  m = len(matrix[0])
  # Create 2 arrays to keep track of rows and cols that contains at least one 0
  col = [0] * m
  row = [0] * n
  
  # Traverse through matrix 
  for i in range(n):
    for j in range(m):
      if matrix[i][j] == 0:
        row[i] = 1
        col[j] = 1

  for i in range(n): 
    for j in range(m):
      if row[i] or col[j]:
        matrix[i][j] = 0
  
  return matrix
  
  
# Optimal Approach
def setZeroes(matrix):
  n = len(matrix)
  m = len(matrix[0])
  col0 = 1
  
  # Step 1: Traverse the matrix and
  # mark 1st row & col accordingly:
  for i in range(n):
    for j in range(m):
      if matrix[i][j] == 0:
        # mark i-th row:
        matrix[i][0] = 0

        # mark j-th column:
        if j != 0:
          matrix[0][j] = 0
        else:
          col0 = 0

  # Step 2: Mark with 0 from (1,1) to (0, m-1):
  for i in range(1, n):
    for j in range(1, m):
      if matrix[i][j] != 0:
        # check for col & row:
        if matrix[i][0] == 0 or matrix[0][j] == 0:
          matrix[i][j] = 0

  #step 3: Finally mark the 1st col & then 1st row:
  if matrix[0][0] == 0:
    for j in range(m):
      matrix[0][j] = 0
  if col0 == 0:
    for i in range(n):
      matrix[i][0] = 0

  return matrix
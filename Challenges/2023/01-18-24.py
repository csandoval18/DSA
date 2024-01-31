# 931. Minimum Falling Path Sum

def minFallingPathSum(matrix: [[int]]) -> int:
  if not matrix:
    return 0

  rows, cols = len(matrix), len(matrix[0])

  for i in range(1, rows):
    for j in range(cols):
      matrix[i][j] += min(matrix[i-1][max(0, j-1):min(cols, j+2)])
  return min(matrix[-1])
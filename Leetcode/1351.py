def countNegatives(grid: [[int]]) -> int:
  n = len(grid)
  m = len(grid[0])
  neg_cnt = 0
  
  for i in range(n-1, -1, -1):
    j = m-1
    while j >= 0 and grid[i][j] < 0:
      neg_cnt += 1
      j -= 1
  
  return neg_cnt
  
  
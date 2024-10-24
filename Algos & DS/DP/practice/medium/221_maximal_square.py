from typing import List


class SolutionRec:
  def maximalSquare(self, matrix: List[List[str]]) -> int:
    if not matrix:
      return 0
      
    n, m = len(matrix), len(matrix[0])
    max_side = 0
    
    def helper(x: int, y: int) -> int:
      if x < 0 or y < 0:
        return 0 # Base case: out of bounds
        
      if matrix[x][y] == '0':
        return 0
      
      # Recurse to check top, left, and top-left diagonal neighbors
      top = helper(x-1, y)
      left = helper(x, y-1)
      top_left = helper(x-1, y-1)
      
      # Current side length
      side = min(top, left, top_left) + 1
      ''' 
      * Why take the minimun of top, left and top-left and add one?
      
      If any any of these squares is smaller, then it restricts the size of the square we can 
      from at the current position (x, y). To maintain a square shape, all three directions
      must contribute equally. Hence, we take the min of these three values,
      ensuring that the current cell can extend to form a square that size, and then add 1
      to account for the inclusison of the current cell.
      '''
      return side
    
    # Check every cell to find the max square
    for x in range(n):
      for y in range(m):
        if matrix[x][y] == '1':
          max_side = max(max_side, helper(x, y))
    
    return max_side ** 2 # Return the area
    
    
class SolutionMemo:
  def maximalSquare(self, matrix: List[List[str]]) -> int:
    if not matrix:
      return 0
    
    n, m = len(matrix), len(matrix[0])
    dp = [[-1] * m for _ in range(n)] 
    max_side = 0
    
    def helper(x: int, y: int) -> int:
      if x < 0 and y < 0:
        return 0
      
      if dp[x][y] != -1:
        return dp[x][y]
      
      if matrix[x][y] == '0':
        return 0
      
      t = helper(x-1, y)
      l = helper(x, y-1)
      tl = helper(x-1, y-1)
      
      dp[x][y] = min(t, l, tl) + 1
      return dp[x][y]
    
    for x in range(n):
      for y in range(m):
        if matrix[x][y] == '1':
          max_side = max(max_side, helper(x, y))
    return max_side ** 2
    
    
class SolutionDP:
  def maximalSquare(self, matrix: List[List[str]]) -> int:
    if not matrix:
      return 0
      
    n, m = len(matrix), len(matrix[0])
    dp = [[0] * m for _ in range(n)]
    max_side = 0
    
    for x in range(n):
      for y in range(m):
        if matrix[x][y] == '1':
          if x == 0 or y == 0:
            dp[x][y] = 1
          else:
            dp[x][y] = min(dp[x-1][y], dp[x][y-1, dp[x-1][y-1]]) + 1
        max_side = max(max_side, dp[x][y])
    return max_side ** 2


class SolutionDP:
  def maximalSquare(self, matrix: List[List[str]]) -> int:
    if not matrix:
      return 0
      
    n, m = len(matrix), len(matrix[0])
    dp = [0] * m
    max_side = 0
    prev = 0 # This will store dp[i-1][j-1] (the diagonal value)
    
    for x in range(n):
      for y in range(m):
        curr = dp[y] # Save the current dp[j] to use it as dp[i-1][j]
        if matrix[x][y] == '1':
          if y == 0:
            dp[y] = 1 
          else:
            dp[j] = min(dp[y], dp[y-1], prev) + 1
          max_side = max(max_side, dp[y])
        else:
          dp[y] = 0 # Reset to 0 if matrix[i][j] = 0
        prev = curr
        
    return max_side ** 2
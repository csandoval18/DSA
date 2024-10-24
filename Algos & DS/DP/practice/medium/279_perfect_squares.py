from math import sqrt

# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other
# words, it is the product of some integer with itself. For example, 1, 4,
# 9, and 16 are perfect squares while 3 and 11 are not.


class SolutionRec:
  def numSquares(self, n: int) -> int:
    # Base case:
    if n == 0:
      return 0
    
    # Initialize the minimum count with a large value
    min_cnt = float('inf')
    
    # Try every perfect sqmath.uare <= n
    for i in range(1, int(sqrt(n)) + 1):
      square = i * i
      min_cnt  = min(min_cnt, 1 + self.numSquares(n - square))
    return min_cnt
      
  
class SolutionMemo:
  def numSquares(self, n: int) -> int:
    dp = [-1] * n
    
    def helper(n: int) -> int:
      if n == 0:
        return 0
        
      if dp[n] != -1:
        return dp[n]
      
      min_cnt = float('inf')
      for i in range(1, int(sqrt(n)) + 1):
        square = i * i
        min_cnt = min(min_cnt, 1 + helper(n-square))
    
      dp[n] = min_cnt
      return min_cnt
    return helper(n)

class SolutionDP:
  def numSquares(self, n: int) -> int:
    dp = [float('inf')] * (n+1)
    dp[0] = 0 # Base case: 0 can be formed by 0 numbers
    
    for i in range(1, n+1):
      for j in range(1, int(sqrt(i)) + 1):
        square = j * j
        dp[i] = min(dp[i], dp[i - square] + 1)
        
    return dp[n]

'''
1. The range of the for loop:
  for i in range(1, int(math.sqrt(n)) + 1):
    
  * i represents the numbers whose square we want to try.
  
  * int(math.sqrt(n)) gives us the largest integer whose square is less than or equal to n.
    - Example: if n = 12, math.sqrt(12) is about 3.46,  so int(math.sqrt(12)) is 3.
    This means we'll try the squares 1,2, and 3 (i.e. 1^2 = 1, 2^2=4, and 3^2 = 9)
    
  * The loop goes fro i = 1 to i = int(math.sqrt(n)). This ensure we check
    all the possible perfect squares 
    
2. Why We Do helper(n - square) and Add 1:
  min_cnt = min(min_cnt, 1 + helper(n - square))
  
  * helper(n - square): We are trying to find out how many more perfect
    squares are needed after subtracting the current square i^2 from n.
    - For example, if n = 12 and i = 2 (so square = 4), we now need to find
      the least number of squares that sum up to 12 - 4 = 8. So, we call helper(8).
    
  * Why add 1: We add 1 because we've used one square (i^2) in the curren step.
  Remember we are returning the least COUNT of perfect squares that are used to sum up to n.
  The recursive call helper(n - square) tells us how many more squares 
  are  needed for he remaining value (n - square)
    - Example: If n = 12 and we use 2^2 = 4, we are left with 8, and if helper(8) 
      find that two more squares are needed for 8, we aadd 1 (for using 4), giving 
      a total of 3 squares.
'''
      
      
n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.

n = 13
# Output: 2
# Explanation: 13 = 4 + 9
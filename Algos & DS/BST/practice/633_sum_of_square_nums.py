import math


class Solution:
  def judgeSquareSum(self, c: int) -> bool:
    def isPerfectSquare(n: int):
      if n < 0:
        return False
      
      sqrt_n = int(math.isqrt(n))
      return sqrt_n * sqrt_n == n
      
    for a in range(int(math.isqrt(c)) + 1):
      b_squared = c - a * a
      if isPerfectSquare(b_squared):
        return True
    return False


c = 5
# Output: true
# Explanation: 1 * 1 + 2 * 2 = 5
s = Solution()
print(s.judgeSquareSum(c))

c = 3
# Output: false
print(s.judgeSquareSum(c))
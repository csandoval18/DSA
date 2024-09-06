from typing import List

# Given an integer n, return an array ans of length n + 1 such that for 
# each i (0 <= i <= n), ans[i] is the number of 1's in the binary 
# representation of i.

# 0, 1, 2, 3, 4, 5
# 0 => 0 = 0
# 1 => 1 = 1
# 2 => 10 = 1
# 3 => 11 = 2
# 4 => 100 = 1
# 5 => 101 = 2

# ans =  [0,1,1,2,1,2]

# i >> 1 shifts the number i one bit to the right, which is equivalent to dividing by 2.

# i & 1 checks whether the least significant bit (the rightmost bit) is 1 (which 
# tells us if i is odd or even). If i & 1 is 1, the number is odd, and if it's 0, the number is even.

class Solution:
  def countBits(self, n: int) -> List[int]:
    res = [0] * (n+1)
    
    for i in range(1, n+1):
      res[i] = res[i >> 1] + (i&1)
      
    return res
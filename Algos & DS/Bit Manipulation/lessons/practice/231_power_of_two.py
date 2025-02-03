# Check if n is a power of: 1, 2, 4, 8, 16, 32, 64...

class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    if n <= 0:
      return False
    return n & (n-1) == 0
      
'''
n = 16
10000 &    n 
01111      n-1
-----
00000 = 0 => True
'''

'''
n = 3
11 &
10
--
10 = 2 => False

- If n is a power of 2, the result will be 0 because the single 1 in n aligns with a 0 in n-1, and all other bits are 0.
- If n is not a power of 2, the result will be non-zero because there will be overlapping 1s in n and n-1.

- If n & (n−1) = 0, it means there are no overlapping 1s between n and n−1.
  This can only happen if n has exactly one bit set to 1, which is the definition of a power of 2.
- If n & (n-1) != 0, it means there are multiple 1s in n, so n is not a power of 2
'''

n = 1
# Output: true
# Explanation: 20 = 1

n = 16
# Output: true
# Explanation: 24 = 16

# n = 3
# Output: false
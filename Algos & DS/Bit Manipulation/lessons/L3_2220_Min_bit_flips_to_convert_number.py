class Solution:
  def minBitFlips(self, start: int, goal: int) -> int:
    x = start ^ goal
    return bin(x).count('1')

start = 10
goal = 7

'''
s = 10
1 0 1 0

g = 7
0 1 1 1

1 0 1 0
0 1 1 1
-------
X X   X = 3 changes
'''

# start = 3
# goal = 4

'''
s = 3
0 1 1

g = 4
1 0 0

0 1 1
1 0 0
-----
X X X = 3 changes

To solve this problem, the XOR operator can be used since it will indicate where the bits are different.

Example:
1 0 1 0 ^
0 1 1 1
-------
1 1 0 1 => 3 flips required to make the numbers equal
'''

s = Solution()
print(s.minBitFlips(start, goal))
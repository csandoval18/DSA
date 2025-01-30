class Solution:
  def checkKthBit(self, n: int, k: int) -> bool:
    return 1 if (1 << k) & n else 0
    # return bin(1 << k)

'''
Remember:
1. First we have a 1 and we left shift it to the kth bit (1 << k)
2. Then we take the result of the left shift by the AND of n. (1 << k) & n
  - If (n & (1 << k)) != 0: = True, then k'th bit is set
  - If (n & (1 << k)) != 0: = False, then k'th bit is not set
   
   1 << 0 = 001
   
   100 ^
   001
   ---
   101
'''

# n = 4
# k = 0
n = 27818
k = 1
# 1011001010010
# 0000000000010
# -------------
# 1011001010000
s = Solution()
print(s.checkKthBit(n, k))
print()
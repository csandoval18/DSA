class Solution:
  def minBitFlips(self, start: int, goal: int) -> int:
    xor_result = start ^ goal
  
    return bin(xor_result).count('1')

start = 10
goal = 7
# 10 -> 1010
#  7 -> 0111

# 1010 -> 1011
# 1011 -> 1111
# 1111 -> 0111


#    1010  (binary of 10)
# ^  0111  (binary of 7)
# ---------
#    1101  (binary result = 13)

# The result 1101 indicates where the bits differ:

# The 1s in the result show which bits need flipping.
# Now, to turn 10 (1010) into 7 (0111), you flip the bits 
# at positions where the result is 1:

# Flip the 1st bit from 1 to 0
# Flip the 2nd bit from 0 to 1
# Flip the 4th bit from 0 to 1
# These 3 flips change 10 to 7. The XOR operation helps
# count the differences, and the bin() function counts how many bits need flipping.
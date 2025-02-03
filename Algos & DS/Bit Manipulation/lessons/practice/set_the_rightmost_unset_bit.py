class Solution:
  def setBit(self, n: int) -> int:
    if (n & (n+1)) == 0: # Checks if all bits are set
      return n
    # Else, set the rightmost unset bit using n and n+1
    return n | (n+1)

n = 6
# Output: 7
# Explanation: The binary representation of 6 is 110. After setting right most bit it becomes 111 which is 7.

n = 15
# Output: 31
# Explanation: The binary representation of 15 is 01111. After setting right most bit it becomes 11111 which is 31.
'''
n = 6

1 1 0 = 6
1 1 1 = 7

1 1 0 &
1 1 1
-----
1 1 0

----------------------------------------------------------------------------------------------------
n = 15

16 8 4 2 1
 0 1 1 1 1 = 15
 1 0 0 0 0 = 16
 
0 1 1 1 1 &
1 0 0 0 0
---------
0 0 0 0 0 = 0


----------------------------------------------------------------------------------------------------

n & (n+1): The bitwise AND operation between n and n + 1 will result in 0 if and only if n has no unset bits (i.e., all bits are 1s). 

This is because:
- If n is of the form (2^k)-1 (e.g., 7 in binary 111), then n + 1 will be 2^k (e.g., 8 in binary 1000). 
  The AND operation between n and n + 1 will be 0 because there are no overlapping 1s.
- If n has at least one unset bit, the AND operation will not result in 0.

3. 

if (n & (n + 1)) == 0:: This condition checks whether n is already a number where all bits are 1s. 
If true, it means there is no unset bit to set, so the function simply returns n.
'''
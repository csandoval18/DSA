'''
Given a positive integer n, determine whether it is odd or even. Return true if the number is even and false if the number is odd.
'''

class Solution:
  def isEven (self, n: int) -> bool:
    return False if n & 1 else True 

'''
To check if a number is even or odd we can simply check the 0'th index bit (right-most bit).
- If the starting bit is 1, then the number will always be odd
- If the starting bit is 0, then the number will always be even
'''

n = 44
# Output: False
s = Solution()
print(s.isEven(n))
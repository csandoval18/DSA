# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

# Test case:
# Input: n = 10, pick = 6
# Output: 6

# Use binary search to find pick


class Solution(object):
  def guessNumber(self, n):
    ans = self.binarySearch(1, n)
    return ans
    
  def binarySearch(l, r):
    # base case 
    if l <= r:
      m = (l + r) // 2
      x = guess(m)
      
      if x == 0:
        return m
      
      if x == 1:
        return self.binarySearch(m, r)
      
      if x == -1:
        return self.binarySearch(l, m)
    else: return -1    
    
      
def guessNumber(self, n):
  l, r = 0, n
  while l <= r:
    m = (l + r)/2

    if guess(m) == -1:
        r = m - 1
    elif guess(m) == 1:
        left = m + 1
    else:
        return m 
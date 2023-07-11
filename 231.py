class Solution(object):
  def isPowerOfTwo(self, n):
    i = 0
    while pow(2, i) < n:
      i += 1
      
    return True if pow(2, i) == n else False
class Solution(object):
    def isPowerOfTwo(self, n):
      if n == 1:
        return True
      
      if n == 2:
        return True
      
      i = 2
      while pow(2, i) < n:
        i += 1
        
      return True if pow(2, i) == n else False
      
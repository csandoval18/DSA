class Solution(object):
  def isPerfectSquare(self, num):
    l, r = 0, num
    ans = binarySearch(l, r, num)
    return ans
    
  def binarySearch(self, l, r, num):
    m = (l + r) // 2
    sq = m * m
    
    if l <= r:
      if sq > num:
        return self.binarySearch(l, m - 1, num)
      elif sq < num:
        return self.binarySearch(m + 1, r, num)
      else:
        return m
        
    return -1
    
    # 16
    #  8 * 8 = 64
    # 64 > 16
    
    # binarysearch(l, m - 1, num)
      
      
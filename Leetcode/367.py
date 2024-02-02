class Solution(object):
  # Recursive Solution
  def isPerfectSquare(self, num):
    l, r = 0, num
    ans = self.binarySearch(l, r, num)
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
        return True
        
    return False
    
    # 16
    # m = 16 / 2 = 8
    #  8 * 8 = 64
    # 64 > 16
    
    # binarysearch(l, m - 1, num)
    
# 
def isPerfectSquare(self, num):
  l, r = 0, num
  
  while l <= r: 
    m = (l + r) // 2
    sq = m * m
    
    if sq > num: 
      r = m - 1
    elif sq < num:
      l = m + 1
    else:
      return True
  return False
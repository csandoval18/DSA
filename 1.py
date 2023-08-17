class Solution(object):
  def twoSum(self, nums, target):
    hm = {}
    
    for i, n in enumerate(nums):
      x = target - n
      
      if x not in hm:
        hm[n] = i
      else:
        return [hm[x], i]
        
    return None
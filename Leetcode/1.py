class Solution(object):
  def twoSum(self, nums, target):
    hm = {}
    res = []
    
    for i, n in enumerate(nums):
      x = target - n
      
      if x not in hm:
        hm[n] = i
      else:
        res.append(hm[n]+1)
        res.append(i+1)
        
    return None
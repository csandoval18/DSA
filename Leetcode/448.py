class Solution(object):
  def findDisappearedNumbers(self, nums):
    n = len(nums)
    
    hm = {key: 0 for key in range(n + 1)}
    
    # Get hm with each element count
    for n in nums:
      if n in hm:
        hm[n] = hm[n] + 1
    
    res = []
    for key, value in hm.items():
      if value == 0:
        res.append(key)
    return res

class Solution(object):
  def findDisappearedNumbers(self, nums):
    res = []
    hm = {}
    
    for n in nums:
      if n not in hm:
        hm[n] = 1
            
    for i in range(1, len(nums) + 1):
      if i not in hm:
        res.append(i)
        
    return res
  
sol = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]

print(sol.findDisappearedNumbers(nums))
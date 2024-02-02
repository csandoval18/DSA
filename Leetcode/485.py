class Solution(object):
  def findMaxConsecutiveOnes(self, nums):
    maxCount = 0
    count = 0
    
    for n in nums:
      if n == 1:
        count += 1
        maxCount = max(maxCount, count)
      elif n != 1:
        count = 0
        
    return maxCount
        
nums = [1, 1, 0, 1, 1, 1]
sol = Solution()   
print(sol.findMaxConsecutiveOnes(nums))
from typing import List


class Solution:
  def sortColors(self, nums: List[int]) -> None:
    n = len(nums)
    l, m, r = 0, 0, n-1
    
    while m <= r:
      if nums[m] == 0:
        nums[l], nums[m] = nums[m], nums[l]
        l += 1
        m += 1
      elif nums[m] == 1:
        m += 1
      else: 
        nums[r], nums[m] = nums[m], nums[r]
        r -= 1
      
    
nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
s = Solution()
print(s.sortColors(nums))
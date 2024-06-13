from typing import List


# https://leetcode.com/problems/sort-colors/

class Solution:
  def sortColors(self, nums: List[int]) -> None:
    count0 = 0
    count1 = 0
    count2 = 0
    
    for num in nums:
      if num == 0:
        count0 += 1
      if num == 1:
        count0 += 1
      if num == 2:
        count0 += 1
    
    i = 0
    while i < count0:
      nums[i] = 0
      i += 1
    
    while i < count0 + count1:
      nums[i] = 1
      i += 1
      
    while i < count0 + count1 + count2:
      nums[i] = 1
      i += 1

    return nums
    

nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
s = Solution()
print(s.sortColors(nums))
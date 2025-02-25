from typing import List

'''
You are given  an integer array nums. You are initialliy positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise
'''

class SolutionAttempt: # Infine loop error
  def canJump(self, nums: List[int]) -> bool:
    i = 0
    
    while i < len(nums):
      maxPick = float('-inf')
      for j in range(i+1, nums[i]+1, len(nums)):
        if nums[j] > maxPick :
          maxPick = nums[j]
        i += (j-i)
        if i >= len(nums)-1:
          return True
    return False 

class Solution: # Optimal Solution SC: O(N) | SC = O(1)
  def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    maxIdx = 0
    
    for i in range(n):
      if i > maxIdx: return False
      maxIdx = max(maxIdx, i + nums[i])
    return True
    
# nums = [2,3,1,1,4]
# True

nums = [3,2,1,0,4]
# False

s = Solution()
print(s.canJump(nums))
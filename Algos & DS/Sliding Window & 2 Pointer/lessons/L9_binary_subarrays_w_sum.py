from typing import List


class SolutionBF:
  def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    cnt = 0
    
    for l in range(len(nums)):
      curr_sum = 0
      
      for r in range(l, len(nums)):
        curr_sum += nums[r]
        
        if curr_sum == goal:
          cnt += 1
        elif curr_sum > goal:
          break
    return cnt


class SolutionBetter: # Does not work, this solution misses other valid subarrays that have a sum of gaol
  def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    l, curr_sum = 0, 0
    cnt = 0
    
    for r in range(len(nums)):
      curr_sum += nums[r]
      
      while curr_sum > goal:
        curr_sum -= nums[l]
        l += 1
    
      if curr_sum == goal:
        cnt += 1
    return cnt
      
      
class SolutionInclusionExclusionPrinciple: # TC: O(n) | SC: O(1)
  def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    def helper(x: int):
      if x < 0:
        return 0
        
      l, curr_sum = 0, 0
      cnt = 0
      
      for r in range(len(nums)):
        curr_sum += nums[r]
        
        while curr_sum > x:
          curr_sum -= nums[l]
          l += 1
        
        cnt += r-l+1
      return cnt
        
    return helper(goal) - helper(goal-1) 
          
    
# nums = [1,0,1,0,1]
# goal = 2
# Output: 4

nums = [0,0,0,0,0]
goal = 0

s = SolutionInclusionExclusionPrinciple()
print(s.numSubarraysWithSum(nums, goal))

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
      
      
class SolutionBetter:
  def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    l, curr_sum = 0, 0
    cnt = 0
    extra_zeroes = 0
    
    for r in range(len(nums)):
      curr_sum += nums[r]
      
      # Shrink the window from the left while the sum exceeds the goal
      while l <= r and curr_sum > goal:
        curr_sum -= nums[l]
        l += 1
      
      # If  the sum equals the goal, count subarrays ending at 'r'
      if curr_sum == goal:
        extra_zeroes 
        
        
    
# nums = [1,0,1,0,1]
# goal = 2
# Output: 4

nums = [0,0,0,0,0]
goal = 0
s = Solution()
print(s.numSubarraysWithSum(nums, goal))

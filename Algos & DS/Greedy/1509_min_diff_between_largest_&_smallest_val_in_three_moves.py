from typing import List


# class Solution:
#   def minDifference(self, nums: List[int]) -> int:
#     average = sum(nums) // len(nums)
#     for num in nums:
      
class Solution:
  def minDifference(self, nums: List[int]) -> int:
    n = len(nums)
    if n <= 4:
      return 0
    
    nums.sort()
    
    # Consider the different scenarios
    return min(nums[-1] - nums[3], # Remove 3 smallest
      nums[-2] - nums[2],          # Remove 2 smallest and 1 largest
      nums[-3] - nums[1],          # Remove 1 smallest and 2 largest
      nums[-4] - nums[0])          # Remove 3 largest

# Example usage
nums = [6, 6, 0, 1, 1, 4, 6]
print(minDifference(nums))  # Output: 2
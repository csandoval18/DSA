from typing import List


class Solution:
  def minSwaps(self, nums: List[int]) -> int:
    n = len(nums)
    total_ones = nums.count(1) # Find total count of ones in nums
    
    # Create the initial window
    current_ones = sum(nums[:total_ones]) # current_ones = sum([1, 0, 1, 0, 1]) = 3
    max_ones_in_window = current_ones # max_ones_in_window = 3
    
    
    # Slide the window over the circular array
    for i in range(1, n):
      current_ones += nums[(i + total_ones - 1) % n] - nums[i - 1] # current_ones += nums[5] - nums[0] = 0 - 1 = -1 => After update curr_ones = 2
      max_ones_in_window = max(max_ones_in_window, current_ones) # max_ones_in_window = max(3,2) = 3
        
    return total_ones - max_ones_in_window

class SolutionModulo: # nums = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0]
  def minSwaps(self, nums: List[int]) -> int:
    n = len(nums)
    total_ones = nums.count(1) # total_ones = 5
    
    # Create the initial window
    current_ones = sum(nums[:total_ones]) # current_ones = sum([1, 0, 1, 0, 1]) = 3
    max_ones_in_window = current_ones # max_ones_in_window = 3
    
    
    # Slide the window over the circular array
    for i in range(1, n):
      current_ones += nums[(i + total_ones - 1) % n] - nums[i - 1] # current_ones += nums[5] - nums[0] = 0 - 1 = -1 => After update curr_ones = 2
      max_ones_in_window = max(max_ones_in_window, current_ones) # max_ones_in_window = max(3,2) = 3
        
    return total_ones - max_ones_in_window

# Example:
nums = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0]


# Output: 1

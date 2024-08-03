class Solution:
  def minSwaps(self, nums: List[int]) -> int:
    n = len(nums)
    total_ones = nums.count(1)
    
    if total_ones == 0:
      return 0
    
    curr_ones = sum(nums[:total_ones])
    max_ones_in_window = curr_ones
    
    extended_nums = nums + nums
    
    for i in range(1, n):
      curr_ones = curr_ones - extended_nums[i-1] + extended_nums[i + total_ones - 1]
      max_ones_in_window = max(max_ones_in_window, curr_ones)

    return total_ones - max_ones_in_window

nums = [0,1,0,1,1,0,0]
# Output: 1

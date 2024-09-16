from typing import List


class Solution:
  def longestSubarray(self, nums: List[int]) -> int:
    max_el = max(nums)  # Step 1: Find the maximum element
    max_len = 0
    curr_len = 0
    
    # Step 2: Find the longest subarray with maximum element
    for num in nums:
      if num == max_el:
        curr_len += 1
        max_len = max(max_len, curr_len)
      else:
        curr_len = 0
    
    return max_len
  
  
 # The key observation is:
# 1. The maximum bitwise AND of any subarray will always be the maximum
# element itself.
# 2. Your task then is to figure out how long the longest sequence of that 
# maximum element is, because the longest contiguous subarray of the 
# maximum element will have the maximum bitwise AND.


# To sum it up: You are looking for the max number repeating in nums that are adjacent to each other.
# Reasoning: This is because when we bitwise AND two or more numbers the bits tend to decrease since the binary numbers compared must both have 1's otheriwse 0 is set
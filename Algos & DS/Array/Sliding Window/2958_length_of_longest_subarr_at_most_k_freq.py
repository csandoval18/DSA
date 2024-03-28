# 2958. Length of Longest Subarray With at Most K Frequency

from collections import defaultdict
from typing import List

def maxSubarrayLength(nums: List[int], k: int) -> int:
  n = len(nums)
  left = 0
  max_length = 0
  hm = defaultdict(int) # Frequenc of els in the curr window
  
  for right in range(n):
    # Add curr element to the window
    hm[nums[right]] += 1
    
    # Shrink the window if the condition is violated
    while max(hm.values()) > k:
      hm[nums[left]] -= 1
      if hm[nums[left]] == 0:
        del hm[nums[left]]
      left += 1
      
    max_length = max(max_length, right - left+1)
  return max_length
  
def maxSubarrayLength(nums: List[int], k: int) -> int:
  n = len(nums)
  l = res = 0
  hm = defaultdict(int)

  for r in range(n):
    hm[nums[r]] += 1  
    while hm[nums[r]] > k:
      hm[nums[l]] -= 1 
      l += 1
    res = max(res, r-l+1)
  return res
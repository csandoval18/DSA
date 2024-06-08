from typing import List


def checkSubarraySum(self, nums: List[int], k: int) -> bool:
  n = len(nums)
  l = 0
  curr_sum = 0
  
  for r in range(n):
    curr_sum += nums[r]
    
    if r-l+1 >= 2 and curr_sum % k == 0:
      return True
      
    curr_sum -= nums[l]
    l += 1
    

      
    

#       0  1 2 3 4
nums = [23,2,4,6,7]
k = 6


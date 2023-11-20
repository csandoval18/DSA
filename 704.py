
from typing import List

def search(nums: List[int], target: int) -> int:
  n = len(nums)
  l = 0
  r = n-1
  
  while l<=r:
    m = (l+r) // 2
    
    if nums[m] == target:
      return m
      
    elif target >= nums[m]:
      l = m+1
    elif target <= nums[m]:
      r = m-1
    
  return -1

nums = [-1,0,3,5,9,12]
print(search(nums, 9))
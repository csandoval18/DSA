from typing import List

def searchInsert(nums: List[int], target: int) -> int:
  n = len(nums)
  l = 0
  r = n-1
  
  while l<=r:
    m = (l+r) // 2
    
    if nums[m] == target:
      return m
    
    elif nums[m] >= target:
      r = m-1
    else:
      l = m+1
    
  return l
      
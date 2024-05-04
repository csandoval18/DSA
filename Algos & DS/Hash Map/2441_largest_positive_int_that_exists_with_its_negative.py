from typing import List

def findMaxK(nums: List[int]) -> int:
  st = set(nums)
  max_k = -1
  
  for num in nums:
    if -num in st and num > 0:
      max_k = max(max_k, num)
  
  return max_k
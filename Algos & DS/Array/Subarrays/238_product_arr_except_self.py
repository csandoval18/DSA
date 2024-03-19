from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
  n = len(nums)
  
  prefix = [1]*n 
  suffix = [1]*n
  res = [0]*n
  
  prefix_product = 1
  for i in range(n):
    prefix[i] = prefix_product
    prefix_product *= nums[i]
    
  suffix_product = 1
  for i in range(n-1, -1, -1):
    suffix[i] = suffix_product
    suffix_product *= nums[i]
  
  for i in range(n):
    res[i] = prefix[i] * suffix[i] 
    
  return res
from typing import List

# BF
def numSubarraysWithSumBF(nums: List[int], goal: int) -> int:
  n = len(nums)
  cnt = 0
  
  for i in range(n):
    prefix_sum = 0
    for j in range(i, n):
      prefix_sum += nums[j]
      if prefix_sum == goal:
        cnt += 1
  return cnt

def numSubarraysWithSumOP(nums: List[int], goal: int) -> int:
  n = len(nums)
  cnt = 0
  l, r = 0, 0
  suff = 0
  
  while l < n:
    suff += nums[r]
    
    if suff == goal:
      cnt += 1
    elif suff > goal:
      l +=  1
    
    
    r += 1
    

nums = [1,0,1,0,1]
goal = 2
print(numSubarraysWithSumOP(nums, goal))
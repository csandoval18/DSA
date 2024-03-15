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


def numSubarraysWithSum1(nums: List[int], goal: int) -> int:
  hm = {}
  hm[0] = 1
  curr_sum = 0
  
  for num in nums:
    curr_sum += num
    if curr_sum - goal in hm:
      res += hm[curr_sum - goal]
    if curr_sum in hm:
      hm[curr_sum] += 1
    else:
      hm[curr_sum] = 1
      
  return res

nums = [1,0,1,0,1]
goal = 2
print(numSubarraysWithSumBF(nums, goal))
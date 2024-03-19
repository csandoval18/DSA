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


# Using dic
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


def numSubarraysWithSum1(nums, goal):
  # Helper function to calc the num of subarrays with sum at most 'goal'
  # So this can have sums <= goal therefore it necessary to subtract from subarrays that
  # have a <= goal-1 sums to get the answer
  def atMost(nums, goal):
    res = left = 0 # Initialize variables for result and left pointer
    
    for right, num in enumerate(nums): # Iterate through array
      goal -= num # Subtract current element from goal
      while goal < 0: # Shrink the window if goal becomes negative
        goal += nums[left]
        left += 1
      # Increment result by the size of the window (number of valid subarrays)
      res += right - left + 1
    return res
  
  # Calculate total number of subarrays with sum exactly equal to 'goal'
  # by subtracting the count of subarrays with sum at most 'goal-1'
  # from the count of subarrays with sum at most 'goal'
  return atMost(nums, goal) - (atMost(nums, goal - 1) if goal > 0 else 0)
  

def numSubarraysWithSum(nums: List[int], goal: int) -> int:
  ans = 0
  hm = {0: 1} 
  count = 0
  
  for num in nums:
    count += num
    ans += hm.get(count-goal, 0)
    hm[count] = hm.get(count, 0) + 1
    
  return ans

nums = [1,0,1,0,1]
goal = 2
print(numSubarraysWithSumBF(nums, goal))
print(numSubarraysWithSum1(nums, goal))
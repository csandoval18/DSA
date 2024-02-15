from typing import List

def findTargetSumWays(nums: List[int], target: int) -> int:
  def bt(idx: int, curr_sum: int) -> int:
    if idx == len(nums):
      if curr_sum == target:
        return 1
      return 0

    
    pos = bt(idx + 1, curr_sum + nums[idx])
    neg = bt(idx + 1, curr_sum - nums[idx])
    
    return pos + neg
  
  return bt(0, 0)

# nums = [1,1,1,1,1]
# target = 3
nums = [1]
target = 1
print(findTargetSumWays(nums, target))

# Memoization
def findTargetSumWays(nums: List[int], target: int, dp: List[int]) -> int:
  def bt(idx: int, curr_sum: int) -> int:
    if idx == len(nums):
      if curr_sum == target:
        return 1
      return 0

    if dp[idx] != int(-1e9):
      return dp[idx]
    
    pos = bt(idx + 1, curr_sum + nums[idx])
    neg = bt(idx + 1, curr_sum - nums[idx])
    
    dp[idx] = pos + neg
    return dp[idx]
  
  dp = [int(-1e9) for _ in range(len(nums))]
  return bt(0, 0)

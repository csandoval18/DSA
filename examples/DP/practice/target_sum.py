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

nums = [1,1,1,1,1]
target = 3
# nums = [1]
# target = 1
print(findTargetSumWays(nums, target))

# Memoization
def findTargetSumWaysMemo(nums: List[int], target: int, dp: List[int]) -> int:
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
  print(dp)
  return bt(0, 0)

print(findTargetSumWays(nums, target))

def findTargetSumWaysTabulation(nums: List[int], target: int) -> int:
  dp = [-1] * (len(nums)+1)
  dp[0] = 0
  curr_sum = 0
  
  for i in range(len(nums)):
    if curr_sum == target:
      dp[i] = 1
  
    pos = curr_sum + nums[i]
    neg = curr_sum - nums[i]
    
    dp[i] = pos + neg
  return dp[i]
    
print(findTargetSumWaysTabulation(nums, target))


def findTargetSumWays(self, nums: List[int], target: int) -> int:
    # Pre-calculate the total sum of the numbers.
    total_sum = sum(nums)

    # If the target is greater than the total sum or not even, return 0.
    if abs(target) > total_sum or (target + total_sum) % 2 != 0:
        return 0

    # Calculate the subset sum we need to achieve.
    subset_sum = (target + total_sum) // 2

    # Create a DP table to store the number of ways to form each subset sum.
    dp = [0] * (subset_sum + 1)
    dp[0] = 1  # There's 1 way to form an empty subset with a sum of 0.

    # Iterate through each number in the input list.
    for num in nums:
        # Iterate backwards from the current subset sum down to the minimum possible
        # value (num - 1). This avoids unnecessary calculations.
        for j in range(subset_sum, num - 1, -1):
            # Add the number of ways to form the current subset sum using the
            # previous subset sum (without the current number) to the number of ways
            # to form the current subset sum using the current number and the previous
            # subset sum (one less than the current subset sum).
            dp[j] += dp[j - num]

    # Return the number of ways to form the target subset sum.
    return dp[subset_sum]


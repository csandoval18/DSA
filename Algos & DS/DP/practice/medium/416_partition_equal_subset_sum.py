from typing import List

class SolutionRec:
  def canPartition(self, nums: List[int]) -> bool:
    total_sum = sum(nums)
    
    # If the total sum is odd, we cannot partition into two equal subsets
    if total_sum % 2 != 0:
      return False
    
    target = total_sum // 2
    
    def helper(i: int, target: int) -> bool:
      # Base cases:
      if target == 0:
        return True
        
      if i == len(nums) or target < 0:
        return False

      # Check if the result is already computed
      # if (i, target) in memo:
      #   return False
      
      # Recursive choices: include or exclude the current number
      include = helper(i+1, target - nums[i])
      exclude = helper(i+1, target)
      return include or exclude
      
    return helper(0, target)
        
      
class SolutionMemo:
  def canPartition(self, nums: List[int]) -> bool:
    total_sum = sum(nums)
    
    if total_sum % 2 != 0:
      return False
    
    target = total_sum // 2
    memo = [[-1] * (target+1) for _ in range(len(nums))]
    
    def helper(i: int, target: int) -> bool:
      if target == 0:
        return True
        
      if i == len(nums) or target < 0:
        return False
      
      if memo[i][target] != -1:
        return memo[i][target]
      
      include = helper(i+1, target - nums[i]) 
      exclude = helper(i+1, target)
      
      memo[i][target] = include or exclude
      return memo[i][target]
    return helper(0, target)
    


class SolutionDP:
  def canPartition(self, nums: List[int]) -> bool:
    total_sum = sum(nums)
    
    # If total sum is odd, we cannot partition into two equal subsets
    if total_sum % 2 != 0:
      return False
    
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True # Base case: a subset with sum 0 is always possible
    
    for num in nums:
      # Traverse backwards to avoid overwriting results from the current iteration
      for  j in range(target, num - 1, -1):
        dp[j] = dp[j] or dp[j - num]
    return dp[target]
      
    
nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1,5,5] and [11].

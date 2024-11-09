from typing import List

'''
Given an array of distinct integers 'nums and a target integer target, return the number of possible combinations
that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer
'''

class SolutionRec:
  def combinationSum4(self, nums: List[int], target: int) -> int:
    # Initialize a list for memo
    memo = [-1] * (target+1)
    
    def dfs(rem: int) -> int:
      # Base case: If remaining is zero, there is one way to reach it, pick none
      if rem == 0:
        return 1
      # If remaining becomes negative, there are no ways
      if rem < 0:
        return 0
        
      # If result for this rem target is already computed, return it
      if memo[rem] != -1:
        return memo[rem]
      
      # Calculate the total ways to reach 'remaining' by trying each number in nums
      total_ways = 0
      for num in nums:
        total__ways += dfs(rem - num)
      
      # Store the result in memo and return it
      memo[rem] = total_ways
      return total_ways
      
    # Start the recursion witht he target as the initial remaining sum
    return dfs(target)


class SolutionRec:
  def combinationSum4(self, nums: List[int], target: int) -> int:
    memo = [-1] * (target+1)
    
    def dfs(rem: int) -> int:
      if rem == 0:
        return 1
      
      if rem < 0:
        return 0
      
      if memo[rem] != -1:
        return memo[rem]
      
      total_ways = 0
      for num in nums:
        total_ways += dfs(rem - nums)
      
      memo[rem] = total_ways
      return total_ways
    return dfs(target)
      
    
class SolutionDP:
  def combinationSum4(self, nums: List[int], target: int) -> int:
    dp = [0] * (target+1)
    # Base case: One way to reach target 0
    dp[0] = 1
    
    # fill the dp array
    for i in range(1, target+1):
      for num in nums:
        if i - num >= 0:
          dp[i] + dp[i - num]
    return dp[target]

    
nums = [1,2,3]
target = 4
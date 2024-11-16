from typing import List

'''
An integer is called arithmetic if:
1. it consists of at least three elements
2. if the difference between any two consecutive elements is the same.
'''

class Solution:
  def numberOfArithmeticSlices(self, nums: List[int]) -> int:
    n = len(nums)
    def helper(i: int, curr_len: int) -> int:
      if i == n:
        if curr_len >= 3:
          res += 1

      for j in range(n):
        res += helper(j) 
        
      
      return res
      
      
class SolutionRec:
  def numberOfArithmeticSlices(self, nums: List[int]) -> int:
    def helper(i: int) -> int:
      if i < 2: # i = 1 or 0
        return 0
      
      slices = helper(i-1)
      if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
        curr_slices = 1 + helper(i-1)
        return slices + curr_slices
      else:
        return slices
    
    return helper(len(nums)-1)
  
  
  class SolutionMemo:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
      n = len(nums)
      memo = [-1]*(n)
      
      def countSlices(i: int):
        if i < 2:
          return 0
          
        if memo[i] != -1:
          return memo[i]
        
        slices = countSlices(i-1)
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
          curr_slices = 1 + countSlices(i-1)
          memo[i] = slices + curr_slices
        else:
          memo[i] = slices
        return memo[i]
      return countSlices(n-1)
      
# 0: i = 3
# if 4 - 3 == 3 - 2: True, therefore this is an arithmetic sequence
#   curr_slices = 1 + helper(2)
# else:
#   return slices 


  
  
  class SolutionDP:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
      n = len(nums)
      if n < 3:
        return 0
      
      dp = [0] * n # dp[i] stores the number of slices ending at i
      total_slices = 0
      
      for i in range(2, n):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
          dp[i] = dp[i-1] + 1
          total_slices += dp[i]
          
      return total_slices
    
      

  #               countSlices(3) = [2,3,4]
  #                 /        \
  #        countSlices(2)    countSlices(1)
  #              /      \
  #     countSlices(1)  Returns 1 (valid slice [1, 2, 3])
  #            /
  # Returns 0 (since i < 2)
  
  # Detailed Tree Walkthrough:
  # 1. Root: countSlices(3):
  #   - Checks slice [2,3,4]
  #   - If valid, moves down to calculate 1 + countSlices(2)
  # 2. Left child: countSlices(2)
  #   - Checks the slice [1,2,3]
  #   - If valid, moves down to calculate 1 + countSlices(1)
  # 3. Left grandchild: countSlices(1)
  #   - This is a base case where (i<2), so it immediately returns 0 because no valid slice can end here.
  # 4. Returning Values:
  #   - countSlices(1) returns 0 up to countSlices(2)
  #   - countSlices(2) then returns 1 up to countSlices(3)
  #   - Finally, countSlices(3) returns 3, accounting for all valid slices ending at indices 2 and 3.



nums = [1,2,3,4]
# Output: 3
# Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

nums = [1]
# Output: 0
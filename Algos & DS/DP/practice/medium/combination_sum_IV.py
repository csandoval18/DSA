from typing import List

'''
Given an array of distinct integers 'nums and a target integer target, return the number of possible combinations
that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer
'''

class Solution:
  def combinationSum4(self, nums: List[int], target: int) -> int:
    memo = [-1] * (target+1)
    
    def dfs(rem: int) -> int:
      # Base case: If remaining is zero, we found one way
      if rem == 0:
        return 1
      # If remaining becomes negative, there are no ways
      if rem < 0:
        return 0
        
      # If result for this rem target is already computed, return it
      if memo[rem] != -1
      
        

nums = [1,2,3]
target = 4
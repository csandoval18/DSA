from typing import List


class SolutionRec:
  def canJump(self, nums: List[int]) -> bool:
    def helper(curr_position: int):
      # Base case: if we have reached or passed the last index
      if curr_position >= n-1:
        return True
      
      # Calculate the furthest index we can jump to
      furthestJump = min(curr_position + nums[curr_position], n-1)
      # Try each possible jump length from 1 to the max jump distance
      for nextPosition in range(nextPosition+1, furthestJump+1):
        if helper(nextPosition):
          return True
      return False
      
    n = len(nums)
    return helper(0)

class SolutionMemo:
  def canJump(self, nums: List[int]) -> bool:
    def helper(i: int):
      # Base case: if we have reached or passed the last index
      if i >= n-1:
        return True
      # If this position is already computed
      if memo[i] != -1:
        return memo[i]
      
      # Calculate the furthest index we can jump to 
      furthestJump = min(i + nums[i], n-1)
      # Try each possible jump length from 1 to the max jump distance
      for j in range(i+1, furthestJump+1):
        if helper(j):
          memo[i] = True 
          return True
      return False
      
    n = len(nums)
    memo = [-1] * n 
    return helper(0)

class SolutionDP:
  def canJump(self, nums: List[int]) -> bool:
    n = len(nums)
    # Initialize the dp array where dp[i] indicates if index i is reachable
    dp = [False] * n
    dp[0] = True
    
    for i in range(n):
      # If the current position is reachable 
      if dp[i]:
        # Update all positions that can be reached from index i
        for j in range(1, nums[i] + 1):
          if i+j < n:
            dp[i+j] = True
    return dp[n-1]
  
    
nums = [2,3,1,1,4]
# Output: true

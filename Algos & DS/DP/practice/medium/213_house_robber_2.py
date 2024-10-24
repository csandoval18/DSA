from typing import List


class SolutionRec:
  def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    return max(self.rob_range(nums, 0, n-2), self.rob_range(nums, 1, n-1))
    
  # Helper function to solve the linear house robber problem for a given range.
  def rob_range(self, nums: List[int],  start: int, end: int):
    # Recursive function with default values of -1 (meaning not computed yet)
    def helper(i: int) -> int:
      if i < start:
        return 0
        
      # Choose to either rob this house or skip it
      pick = self.rob_recursive(i-1)
      notPick = nums[i] + self.rob_recursive(i-2)
      return max(pick, notPick)
    # Call the recursive function starting from the end of the range.
    return helper(end)


class SolutionMemo:
  def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    return max(self.rob_range(nums, 0, n-2), self.rob_range(nums, 1, n-1))
    
  # Helper function to solve the linear house robber problem for a given range.
  def rob_range(self, nums: List[int],  start: int, end: int):
    # Create a list for memoization with default values of -1 (meaning not computed yet).
    dp = [-1] * len(nums)
    # Recursive function with default values of -1 (meaning not computed yet)
    def helper(i: int) -> int:
      if i < start:
        return 0
      if dp[i] != -1:
        return dp[i]
        
      # Choose to either rob this house or skip it
      pick = self.rob_recursive(i-1)
      notPick = nums[i] + self.rob_recursive(i-2)
      dp[i] = max(pick, notPick)
      return dp[i]
    # Call the recursive function starting from the end of the range.
    return helper(end)
    

class SolutionDP:
  def rob(self, nums: List[int]) -> int:
    if len(nums) == 1:
      return nums[0]
    # Compare two cases: rob from 0 to n-2 and from 1 to n-1.
    return max(self.rob_linear(nums, 0, len(nums)-2), self.rob_linear(nums, 1, len(nums)-1))
    
  # Helper function to solve the linear house robber problem using dynamic programming.
  def rob_linear(self, nums: List[int], start: int, end: int) -> int:
    if start == end:
      return nums[start]
      
    # Initialize two variables to store the max amount 
    prev2, prev1 = 0, 0
    # Loop through the houses in the range [start, end].
    for i in range(start, end+1):
      # Current value is either rob this house (nums[i] + prev2) or skip it (prev1).
      pick = nums[i] + prev2
      notPick = prev1
      curr = max(pick, notPick)
      # Update prev2 and prev1 for the next iteration
      prev2, prev1 = prev1, curr
    return prev1

nums = [2,3,2]
s = SolutionDP()
print(s.rob(nums))

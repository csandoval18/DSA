from typing import List


class SolutionRec:
  def jump(self, nums: List[int]) -> int:
    def helper(i: int):
      # Base case: If we're at the last index, no more jumps needed
      if i == n-1:
        return 0
      
      # Initialize the main jumps to a large number
      min_jumps = float('inf')
      # Explore all possible next positions from the current index
      for j in range(i+1, min(i + nums[i] + 1, n)):
        nm = helper(j)
        min_jumps = min(min_jumps, nm)
        
      return min_jumps
    
    n = len(nums)
    # Start from the first index with 0 jumps
    return helper(0)
    
class SolutionMemo:
  def jump(self, nums: List[int]) -> int:
    def helper(i: int) -> int:
      if i == n-1:
        return 0
      
      # If we have already computed the result for this index, return it
      if i in memo:
        return memo[i]
      
      min_jumps = float('inf')
      for j in range(i+1, min(i + nums[i] + 1, n)):
        min_jumps = min(min_jumps, 1 + helper(j)) # Take a jump and add the result
      
      # Store the result in memo to avoid recomputation
      memo[i] = min_jumps
      return memo[i]
      
    n = len(nums)
    memo = [-1]*n # Array to store the minimum jumps from each index, initialized to -
    return helper(0)
    
class SolutionDP:
  def jump(self, nums: List[int]) -> int:
    

nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. 
# Jump 1 step from index 0 to 1, then 3 steps to the last index.
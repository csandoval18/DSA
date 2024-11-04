from typing import List

'''
A wiggle sequence is a sequence where the differences between successive numbers strictly
alternate between positive and negative. The first difference (if one exists) may be either
postiive or negative. A sequence with one element and a sequence with two non-equal
elements are trivially wiggle sequences.
'''


# isUp = True | expecting an "up" wiggle, previous wiggle was "down"
# isUp = False | expecting a "down" wiggle, previous wiggle was "up"
class SolutionRec:
  def wiggleMaxLength(self, nums: List[int]) -> int:
    def dfs(i: int, isUp: bool) -> int:
      if i == len(nums):
        return 0
      
      length = dfs(i+1, isUp) # Skip current element
      # Check if current el can be part of the wiggle sequence
      if (isUp and nums[i] > nums[i-1]) or (not isUp and nums[i] < nums[i-1]):
        length = max(length, 1 + dfs(i+1, not isUp)) # Take current el and switch direction
      
      return length
        
    if len(nums) < 2:
      return len(nums)
    # The initial 1 + part accounts for the first element (nums[0]), which we always include as the beginning of the wiggle sequence.
    return 1 + max(dfs(1, True), dfs(1, False))


class Solution:
  def wiggleMaxLength(self, nums: List[int]) -> int:
    def dfs(i: int, isUp) -> int:
      if i == len(nums):
        return 0
      
      if memo[i][isUp] != -1: 
        return memo[i][isUp]
      
      maxLen = dfs(i+1, isUp)
      if (isUp and nums[i] > nums[i-1]) or (not isUp and nums[i] < nums[i-1]):
        maxLen = max(maxLen, 1 + dfs(i+1, not isUp))
      return maxLen
    
    memo = [[-1] * 2 for _ in range(len(nums))]
    
      
        
        
        
    

nums = [1,7,4,9,2,5]
# Output: 6
# Explanaition: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

nums = [1,17,5,10,,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that ahieve this length.
# One is [1,17,10,13,10,16,8] with differences (16,-7,3,-3,6,-8)

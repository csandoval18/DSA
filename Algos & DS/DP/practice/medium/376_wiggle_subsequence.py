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


class SolutionMemo:
  def wiggleMaxLength(self, nums: List[int]) -> int:
    def dfs(i: int, isUp: int) -> int:
      if i == len(nums): # This just means the recursion loop goes in range(1, n)
        return 0
      
      if memo[i][isUp] != -1:
        return memo[i][isUp]
      
      maxLen = dfs(i+1, isUp)
      if (isUp == 1 and nums[i] > nums[i-1]) or (isUp == 0 and nums[i] < nums[i-1]):
        maxLen = max(maxLen, 1 + dfs(i+1, isUp ^ 1))

      memo[i][isUp] = maxLen
      return maxLen
    
    if len(nums) < 1:
      return len(nums)

    n = len(nums)
    memo = [[-1]*2 for _ in range(n)]
    return 1 + max(dfs(1, 1), dfs(1, 0))
  
  
class SolutionDP:
  def wiggleMaxLength(self, nums: List[int]) -> int:
    if len(nums) < 2:
      return len(nums)
    
    n = len(nums)
    # Initialize the dp table
    dp = [[1, 1] for _ in range(n)]
    
    # Fill the dp table
    for i in range(1, n):
      for j in range(i):
        if nums[i] > nums[j]:  # current wiggle goes up
          dp[i][1] = max(dp[i][1], dp[j][0] + 1)
        elif nums[i] < nums[j]:  # current wiggle goes down
          dp[i][0] = max(dp[i][0], dp[j][1] + 1)
    
    # The result is the longest wiggle sequence ending either up or down
    return max(dp[i][0], *(dp[i][1] for i in range(n)))      

class SolutionDP:
  def wiggleMaxLength(self, nums: List[int]) -> int:
    if not nums:
      return 0
      
    n = len(nums)
    # dp = [[0]*2 for _ in range(n+1)]
    dp = [[1, 1] for _ in range(n)]
    
    for i in range(1, n):
      if nums[i] > nums[i-1]:
        dp[i][1] = dp[i-1][0] + 1 # Extend the sequence ending in down
        dp[i][0] = dp[i-1][0] # Carry over the previous "down" sequence
      elif nums[i] < nums[i-1]:
        dp[i][0] = dp[i-1][1] + 1 # Extend the sequence ending in up
        dp[i][1] = dp[i-1][1] # Carry over the previous "up" sequence
      else:
        # If nums[i] == nums[i-1], carry over both  states
        dp[i][0] = dp[i-1][0]
        dp[i][1] = dp[i-1][1]
      
    # The result is the max wiggle length considering both up and down at the last index
    return max(dp[n-1][0], dp[n-1][1])
    

nums = [1,7,4,9,2,5]
# Output: 6
# Explanaition: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

# nums = [1,17,5,10,,13,15,10,5,16,8]
# Output: 7
# Explanation: There are several subsequences that ahieve this length.
# One is [1,17,10,13,10,16,8] with differences (16,-7,3,-3,6,-8)

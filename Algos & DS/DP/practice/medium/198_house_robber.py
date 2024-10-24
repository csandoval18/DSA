from typing import List


class SolutionRec:
  def rob(self, nums: List[int]) -> int:
    n = len(nums)
    
    def helper(i: int) -> int:
      if i < 0:
        return 0
        
      notPick = helper(i-1)
      pick = nums[i] + helper(i-2)
      return max(notPick, pick)
      
    return helper(n-1)
    
    
class SolutionMemo:
  def rob(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [-1] * (n+1)
    
    def helper(i: int) -> int:
      if i < 0:
        return 0
        
      if dp[i] != -1:
        return dp[i]
      
      pick = nums[i] + helper(i-2)
      notPick = nums[i-1]
      dp[i] = max(pick, notPick)
      return dp[n]
    return helper(n-1)
      
      
class SolutionDP:
  def rob(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [-1] * (n+1)
    dp[0] = 0
    dp[1] = nums[0]
    
    for i in range(2, n):
      pick = nums[i] + dp[i-2]
      notPick = dp[i-1]
      dp[i] = max(pick, notPick)
    return dp[n-1]
  
nums = [2,3,2]    
# Output: 3

nums = [1,2,3,1]
# Output: 4

nums = [1,2,3]
# Output: 3
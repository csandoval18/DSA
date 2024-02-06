from typing import List

# Recursive Solution 
def maximumNonAdjacentSumRecursive(nums: List[int]) -> int:
  def helper(idx: int) -> int:
    if idx == 0:
      return nums[idx]
    if idx < 0:
      return 0
    
    pick = nums[idx] + helper(idx-2)
    not_pick = 0 + helper(idx-1)
    return max(pick, not_pick)
    
  n = len(nums)
  return helper(n-1)
  
# DP
def maximumNonAdjacentSumDP(nums: List[int]) -> int:
  n = len(nums)
  dp = [0]*(n+1)
  dp[0] = nums[0]
  
  for i in range(1, n):
    # This wouldnt work since in the recursive solution there is an edge case for f(-1)
    # take =  nums[i] + dp[i-2]
    take = nums[i] 
    if i > 1:
      take += dp[i-2] 
    # non take because we are going into the adjacent num idx
    nontake = 0 + dp[i-1]
    
    dp[i] = max(take, nontake)

# DP w/ space optmized
def maximumNonAdjacentSum(nums: List[int]) -> int:
  n = len(nums)
  prev = nums[0]
  prev2 = 0
  
  for i in range(1, n):
    take = nums[i]
    if i>1:
      take += prev2
    notTake = 0 + prev
    
    tmp = max(take, notTake)
    prev2 = prev
    prev = tmp
  return prev
    
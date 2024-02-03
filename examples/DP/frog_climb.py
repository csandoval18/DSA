from typing import List

def frogJump(n: int, heights: List[int]) -> int:
  def backtrack(idx: int, dp: List[int]) -> int:
    if idx == 0:
      return 0
    
    if dp[idx] != -1:
      return dp[idx]
    
    left = backtrack(idx-1, dp) + abs(heights[idx] - heights[idx-1])
    
    right = float('inf')
    if idx > 1:
      right = backtrack(idx-2, dp) + abs(heights[idx] - heights[idx-2])
    
    res = min(left, right)
    dp[idx] = res
    return res
  
  dp = [-1]*(n+1)
  return backtrack(n-1, dp)
    
    
arr = [30,10,60,10,60,50] 
n = 6
print(frogJump(n, arr))
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


# Bottom up Tabulation
def frogJump(n: int, heights: List[int]) -> int:
  dp = [-1]*(n+1)
  dp[0] = 0
  
  for i in range(n):
    fs = dp[i-1] + abs(heights[i]-heights[i-1])
    if i > 1:
      ss = dp[i-1] + abs(heights[i]-heights[i-1])
    
    dp[i] = min(fs, ss)
  
  return dp[n-1]
      
# Space Optimized
def frogJump(n: int, heights: List[int]) -> int:
  prev = 0
  prev2 = 0
  
  for i in range(1, n):
    fs = prev + abs(heights[i] - heights[i-1])
    
    ss = float('inf')
    if i > 1:
      ss = prev2 + abs(heights[i] - heights[i-2])
    
    curr = min(fs, ss) 
    prev2 = prev
    prev = curr
    
  return prev
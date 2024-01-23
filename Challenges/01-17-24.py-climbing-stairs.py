def climbingStairs(n: int) -> int:
  dp = [0] * (n+1)
  dp[1] = 1
  dp[2] = 1
  
  for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]
  
  return dp[n]
  
# Leetcode asks for fibonacci based on 0 starting index
# 1 1 2 3 5 8 7  8 
# 0 1 2 3 4 5 6 7
def climbingStairsLC(n: int) -> int:
  dp = [0] * (n+1)
  dp[0] = 1
  dp[1] = 1
  
  for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]
  
  return dp[n]
  
print(climbingStairsLC(2))

1,1,2,3,5,8,13,21,34
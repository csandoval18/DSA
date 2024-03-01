from typing import List

# Memoization
def lcsMemo(s1: str, s2: str) -> int:
  def f(i1: int, i2: int, dp: List[List[str]]) -> int:
    # Base case: If either of the strings ahs reached the end (0)
    if i1 < 0 or i2 < 0:
      return 0
    
    # If the result for this state is already calculated, return it
    if dp[i1][i2] != -1:
      return dp[i1][i2]
    
    # If the chars at the curr idxs match, include them in the lcs
    if s1[i1] == s2[i2]:
      dp[i1][i2] = 1 + f(i1-1, i2-1, dp)
    else:
      # If the chars do not match, consider both possibilities:
      # 1. Exclude chars from s1 and continue matching in s2
      # 2. Exclude chars from s2 and continue matching in s1
      dp[i1][i2] = max(f(i1, i2-1, dp), f(i1-1, i2, dp))
    
    return dp[i1][i2]
  
  n = len(s1)
  m = len(s2)
  dp = [[-1 for _ in range(m)] for _ in range(n)]
  return f(n-1, m-1, dp)
  
def lcsTab(s1: str, s2: str) -> int:
  n, m = len(s1), len(s2)
  dp = [[0]*(m+1) for _ in range(n)]
  
  # Initialize the base cases: (Don't need it since it just intializes firt row 
  # and col to 0's
  # for i in range(n+1):
  #   dp[i][0] = 0
  # for j in range(m+1):  
  #   dp[0][j] = 0

  for i in range(1, n+1):
    for j in range(1, m+1):
      if s1[i-1] == s2[j-1]:
        # if the chars match, increment the LCS length
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        # If the chars do not match, take the max of
        # lcs length without one char from s1 or s2
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])

  return dp[n][m]
        
s1 = "acd"
s2 = "ced"
print(lcsMemo(s1, s2))
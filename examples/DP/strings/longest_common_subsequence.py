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
      dp[i1][i2] = 1 + lcsMemo(i1-1, i2-1, dp)
    else:
      # If the chars do not match, consider both possibilities:
      # 1. Exclude chars from s1 and continue matching in s2
      # 2. Exclude chars from s2 and continue matching in s1
      dp[i1][i2] = max(f(s1, s2, i1-1, i2-1, dp))
    
    return dp[i1][i2]
  
  n = len(s1)
  m = len(s2)
  dp = [[-1 for _ ]]
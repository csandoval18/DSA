from typing import List

# 115. Distinct Subsequences
# Given two strings s and t, return the number of distinct subsequences of s which equals t.
# The test cases are generated so that the answer fits on a 32-bit signed integer.

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# (rabb) b (it)
# (ra) b (bbit)
# (rab) b(bit)

def numDisctinctRec(s: str, t: str) -> int:
  def f(i: int, j: int) -> int:
    if j < 0:
      return 1
    if i < 0:
      return 0
    
    if s[i] == t[j]:
      return f(i-1, j-1) + f(i-1, j)
    return f(i-1, j)
  
  n, m = len(s), len(t)
  return f(n-1, m-1)
  
def numDistinctMemo(s: str, t: str):
  def f(i: int, j: int, dp: List[List[int]]) -> int:
    # If we have exhausted s2, we found a valid subsequence
    if j < 0:
      return 1
    # If we have exhausted s1, but not s2, no valid subsequence found
    if i < 0:
      return 0
    
    # If this subproblem has already been solved, return the cached res
    if dp[i][j] != -1:
      return dp[i][j]
    
    # If the curr chars match, we can either choose to leave one chars 
    # or stay with the curr chars in s1iafdxxafda
    if s[i] == t[j]:
      dp[i][j] = f(i-1, j-1, dp) + f(i-1, j, dp)
      return dp[i][j]
    
    dp[i][j] = f(i-1, j, dp)
    return dp[i][j]
      
  n, m = len(s), len(t)
  # Initialize a dp table to store the intermediate results
  dp = [[-1 for _ in range(m)] for _ in range(n)]
  return f(n-1, m-1, dp)

def numDistinctMemoUpdate(s: str, t: str):
  def f(i: int, j: int, dp: List[List[int]]) -> int:
    # If we have exhausted s2, we found a valid subsequence
    if j == 0:
      return 1
    # If we have exhausted s1, but not s2, no valid subsequence found
    if i == 0:
      return 0
    
    # If this subproblem has already been solved, return the cached res
    if dp[i][j] != -1:
      return dp[i][j]
    
    # If the curr chars match, we can either choose to leave one chars 
    # or stay with the curr chars in s1
    if s[i-1] == t[j-1]:
      dp[i][j] = f(i-1, j-1, dp) + f(i-1, j, dp)
      return dp[i][j]
    
    dp[i][j] = f(i-1, j, dp)
    return dp[i][j]
      
  # Initialize a dp table to store the intermediate results
  n, m = len(s), len(t)
  dp = [[-1 for j in range(m+1)] for i in range(n+1)]
  return f(n, m, dp)
      
def numDistinctTab(s: str, t: str):
  n, m = len(s), len(t)
  dp = [[0]*(m+1) for _ in range(n+1)]
  
  for i in range(n+1):
    dp[i][0] = 1
  
  # for j in range(1, m+1):
  #   dp[0][j] = 0 
  
  for i in range(1, n+1):
    for j in range(1, m+1):
      if s[i-1] == t[j-1]:
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
      else:
        dp[i][j] = dp[i-1][j]

  return dp[n][m]
  
def numDistinctSO(s: str, t: str):
  n, m = len(s), len(t)
  prev = [0]*(m+1)
  prev[0] = 1
  
  for i in range(1, n+1):
    curr = []
    for j in range(m, 0, -1):
      if s[i-1] == t[j-1]:
        prev[j] = prev[j-1] + prev[j]
      # else:
      #   prev[j] = prev[j]

  return prev[m]
      
# s1 = "babgbag" 
# s2 = "bag"
s = "rabbbit"
t = "rabbit"

print(numDisctinctRec(s, t))
print(numDistinctMemo(s, t))
print(numDistinctMemoUpdate(s, t))
print(numDistinctTab(s, t))
print(numDistinctSO(s, t))
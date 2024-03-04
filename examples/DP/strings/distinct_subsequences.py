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

def numDisctinct(s: str, t: str) -> int:
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
  
def subsequenceCounting(s: str, t: str, n: int, m: int):
  def countUtil(i: int, j: int, dp: List[List[int]]) -> int:
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
    # or stay with the curr chars in s1
    if s[i] == t[j]:
      leaveOne = countUtil(i-1, j-1, dp)
      stay = countUtil(i-1, j, dp)
      
      # Store the res in the dp table and return it modulo prime
      dp[i][j] = (leaveOne + stay) % prime
      
  # Initialize a dp table to store the intermediate results
  dp = [[-1 for j in range(m)] for i in range(n)]
  prime = int(1e9 + 7)

def subsequenceCounting(s: str, t: str, n: int, m: int):
  dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
  
  # Base case
  for i in range(n+1):
    dp[i][0] = 1
  
  # Initialize dp[0][j] to 0 for j > 0 since an empty s can't have 
  # a non-empty subsequence  
  # for j in range(1, m+1):
  #   dp[0][i] = 0
  
  # Fill in the dp table using dynamic programming
  for i in range(1, n+1):
    for j in range(1, m+1):
      # If the curr chars match, we have two choices:
      # 1. Include the current chars in both s1 and s2 (dp[i-1][j-1])
      # 2. Skip the curr character in s1 (dp[i-1][j])

# s1 = "babgbag" 
# s2 = "bag"
s = "rabbbit"
t = "rabbit"
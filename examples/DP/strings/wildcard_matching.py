from typing import List

def isMatchMemo(s: str, p: str) -> bool:
  def f(i: int, j: int, dp: List[List[bool]]) -> int:
    # Base cases
    # s is exhausted and p is exhausted
    if  i < 0 and j < 0:
      return True
    # if s is exhausted, p > 0
    if i < 0 and j >= 0:
      return False
    # if s > 0, p is exhausted
    if i >= 0 and j < 0:
      for j in range(i+1):
        if s[j] != "*":
          return False
      return True
    
    # Look for overlapping subproblems
    if dp[i][j] != -1:
      return dp[i][j]
    
    if s[i] == p[j] or s[i] == "?":
      # If chars match or s1 has a '?', then we move both pointers 
      dp[i][j] = f(i-1, j-1, dp)
    elif s[i] == "*":
      dp[i][j] = f(i-1, j, dp) or f(i, j-1, dp)
    else:
      dp[i][j] = False
    
    return dp[i][j]
  
  n, m = len(s), len(p)
  dp = [[False]*(m) for _ in range(n+1)]
  return f(n-1, m-1, dp)
      
def isMatchTab(s: str, p: str) -> bool:
  n, m = len(s), len(p)
  dp = [[False]*(m+1) for _ in range(n+1)]
  
  # Initialize dp[0][0] to True since two empty strings match
  dp[0][0] = True
  
  # Initialize the first row of dp
  for j in range(1, m):
    dp[0][j] = False
  
  for i in range(1, n+1):
    for j in range(1, i+1):
      if s[j-1] != '*':
        dp[i][0] = False
      else:
        dp[i][0] = True
    
  # Initailize first col of dp based on weather s consists of all '*' chars
  for i in range(1, n+1):
    for j in range(1, m):
      if s[i-1] == p[j-1] or s[i-1] == '?':
        dp[i][j] = dp[i-1][j-1]
      elif s[i-1] == '*':
        # If s has a '*', there are two choices:
        # 1. '*' represents an empty string in s, so move to the prev chars in s (i-1, j).
        # 2. '*' represents one or more chars in s, so move to the prev chars in p (i, j-1).
        dp[i][j] = dp[i-1][j]  or dp[i][j-1]
      else:
        dp[i][j] = False
  
  # The final val in dp[n][m-1] is True if the two string match, False otherwise
  return dp[n][m]

def isMatchSO(s: str, p: str) -> bool: 
  def isAllStars(s, i):
    # Helper function to check if all chars up to the index i in string s are '*'
    for  j in range(1, i+1):
      if s[j-1] != '*':
        return False
    return True
    
  n, m = len(s), len(p)
  prev = [False for _ in range(m+1)]
  curr = [False for _ in range(m+1)]
  
  prev[0] = True # Initialize the first element of prev to True
  
  for i in range(1, n+1):
    curr[0] = isAllStars(s, i)
    for j in range(1, m+1):
      if s[i-1] == p[j-1] or s[i-1] == '?':
        curr[j] = prev[j-1]
      elif s[i-1] == '*':
        curr[j] = prev[j] or curr[j-1]
      else:
        curr[j] = False
    prev = curr
  
  return prev[m]

s = 'ab*cd'
p = 'abdefcd'
print(isMatchMemo(s, p))
print(isMatchTab(s, p))
print(isMatchSO(s, p))
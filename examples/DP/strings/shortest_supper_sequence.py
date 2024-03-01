from ast import List

def shortestSupersequence(s1: str, s2: str):
  n, m = len(s1), len(s2)
  dp = [[0]*(m+1) for _ in range(n+1)]
  
  # for i in range(n+1):
  #   dp[i][0] = 0
  # for j in range(m+1):
  #   dp[0][i] = 0
  
  # This code finds the LCS of the strings
  for i in range(1, n+1):
    for j in range(1, m+1):
      if s1[i-1] == s2[i-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
  
  # Initialize 2 pointers for the strings
  size = dp[n][m]
  i, j = n, m
  
  index = size-1
  res = ""
  
  while i > 0 and j > 0:
    if s1[i-1] == s2[j-1]:
      res += s1[i-1]
      index -= 1
      i -= 1
      j -= 1
    elif dp[i-1][j] > dp[i][j-1]:
      res += s1[i-1]
      i -= 1
    else:
      res += s2[j-1]
      j -= 1
  
  # Adding remaining chars for uneven string lengths
  while i > 0:
    res += s1[i-1]
    i -= 1
  while j > 0:
    res += s2[j-1]
    j -= 1
  
  res = res[::-1]
  return res
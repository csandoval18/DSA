def minInsertions(s: str) -> int:
  n = len(s)
  p = s[::-1]
  dp = [[0]*(n+1) for _ in range(n+1)]
  
  # Base case
  # dp[0][0] = 0
  
  for i in range(1, n+1):
    for j in range(1, n+1):
      if s[i-1] == p[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
  return n - dp[n][n]


# s = 'abcivicxz'
s = "leetcode"
print(minInsertions(s))
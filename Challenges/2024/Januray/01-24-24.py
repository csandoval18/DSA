def longestCommonSubsequence(text1: str, text2: str) -> int:
  def LCS(text1: str, text2: str, i: int, j: int) -> int:
    # Base case: When reither of the strings is empty
    if i == 0 or j == 0:
      return 0
      
    # If the current characters match
    if text1[i-1] == text2[j-1]:
      return 1 + longestCommonSubsequence(text1, text2, i-1, j-1)
    else:
      # If the current chars dont match, cosider two cases:
      # 1. Exclude the last chars of text1
      # 2. Exclude the last chars of text2
      return max(longestCommonSubsequence(text1, text2, i-1, j), longestCommonSubsequence(text1, text2, i, j-1))

def longestCommonSubsequence(text1, text2):
  n, m = len(text1), len(text2)
  dp = [[0] * (m + 1) for _ in range(n + 1)]

  for i in range(1, n + 1):
    for j in range(1, m + 1):
      if text1[i - 1] == text2[j - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

  return dp[n][m]
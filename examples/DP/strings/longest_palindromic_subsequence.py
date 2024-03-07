from typing import List

# 516. Longest Palindromic Subsequence
  
# This solution generates all subsequences and searches checks if they are all palindromes 
# then the longest palindrome found is returned

def longestPalindromeSubseqVer1AllSubsets(s: str) -> int:
  def isPalindrome(string: str) -> bool:
    return string == string[::-1]
    
  def f(i: int, ds: str) -> int:
    if i < 0:
      if isPalindrome(ds):
        return len(ds)
      else:
        return 0
    
    # Include the curr char in the subsequence
    pick = f(i-1, s[i] + ds)
    notPick = f(i-1, ds)
    
    return max(pick, notPick)
  
  n = len(s)
  return f(n-1, "")


# Recursion
def longestPalindromeSubseqRec(s: str) -> int:
  def lcs(i, j):
    if i == 0 or j == 0:
      return 0
    
    if s[i-1] == t[j-1]:
      return 1 + lcs(i-1, j-1)
      
    return max(lcs(i-1, j), lcs(i, j-1))
  
  t = s[::-1]
  n = len(s)
  return lcs(n, n)


# Memoization
def longestPalindromeSubseqMemo(s: str) -> int:
  def lcs(i: int, j: int, dp: List[List[int]]):
    if i == 0 or j == 0:
      return 0
    
    if dp[i][j] != -1:
      return dp[i][j]
    
    if s[i-1] == t[j-1]:
      return 1 + lcs(i -1, j-1, dp)
      
    return max(lcs(i-1, j, dp), lcs(i, j-1, dp))
  
  
# Tabulation
def longestPalindromeSubseqTab(s: str) -> int:
  n = len(s)
  p = s[::-1]
  dp = [[0]*(n+1) for _ in range(n+1)]
  dp[0][0] = 0
  
  for i in range(1, n+1):
    for j in range(1, n+1):
      if s[i-1] == p[j-1]:
        dp[i][j] = 1 + dp[i-1][j-1]
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
  return dp[n][n]

s = "cbbd"
# output: 2
print(longestPalindromeSubseqVer1AllSubsets(s))
print(longestPalindromeSubseqRec(s))
print(longestPalindromeSubseqTab(s))
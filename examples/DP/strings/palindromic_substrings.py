# Doesn't work
# Tried generating all substring, then checking if they were palindromes.
def countSubstringsAttempt(s: str) -> int:
  def isPalindrome(s: str) -> bool:
    return s == s[::-1]
    
  def f(i: int, ds: str) -> int:
    if i < 0:
      print(ds)
      if isPalindrome(ds):
        return 1
      else:
        return 0

    pick = f(i-1, s[i] + ds)
    notPick = f(i-1, ds)

    return pick + notPick
  
  n = len(s)
  return f(n-1, "")


def countSubstrings(s: str) -> int:
  n = len(s)
  dp = [[False]*n for _ in range(n)]
  res = 0
  
  # Base case: single char substrings
  for i in range(n):
    dp[i][j] = True
    count += 1
  
  # Base case: two consecutive similar chars
  for i in range(n-1):
    if s[i] == s[i+1]:
      dp[i][i+1] = True
      res += 1
  
  # General case: substring of length 3 to n
  for length in range(3, n+1):
    for i in range(n-length+1):
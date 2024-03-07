# 516. Longest Palindromic Subsequence
  
# This solution generates all subsequences and searches checks if they are all palindromes 
# then the longest palindrome found is returned
def longestPalindromeSubseqVer1Rec(s: str) -> int:
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



# Find lcs of s and s[::-1]
def longestPalindromeSubseq(self, s: str) -> int:
  

s = "cbbd"
# output: 2
print(longestPalindromeSubseqVer1Rec(s))
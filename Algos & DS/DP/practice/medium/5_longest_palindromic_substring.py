class Solution:
  def isPalindrome(s: str):
    return s == s[::-1]
  
  def isPalindromeRec(self, s: str, left: int, right: int) -> bool:
    # Base case: if the pointers have crossed each other, it's a palindrome
    if left >= right:
      return True
    # If characters at current positions are not equal, it's not a palindrome
    if s[left] != s[right]:
      return False
    
    # Recursively check the remaining substring
    return self.isPalindromeRec(s, left+1, right-1)
    
  def longestPalindrome(self, s: str) -> str:
    n = len(s)
    if n == 0:
      return ""
      
    def helper(left: int, right: int, longest: str) -> str:
      if left == n:
        return longest
      
      # Recursively check for palindromes expanding around the current character
      
  
s = "babad"
# Output: "bab"

class Solution:
  def longestPalindrome(self, s: str) -> str:
    def isPalindrome(s: str):
      return s == s[::-1]
      
    def helper(i: int, ds: str):
      if i == len(s):
        return 
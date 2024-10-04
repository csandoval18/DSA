class Solution1:
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

    # Helper function to recursively find the longest palindrome
    def helper(left: int, right: int, longest: str) -> str:
      if left == n:  # Base case: when we've checked all characters
        return longest

      # Recursively check for palindromes expanding around the current character
      for j in range(left, n):
        if helper(s, left, j):
          current_palindrome = s[left:j + 1]
          if len(current_palindrome) > len(longest):
            longest = current_palindrome

      # Recursive call for the next starting point (left+1)
      return helper(left + 1, right, longest)

    # Start the recursion from the first character
    return helper(0, n - 1, "")

class Solution:
  def isPalindrome(self, s: str) -> bool:
    return s == s[::-1]
  
  def longestPalindrome(self, s: str) -> str:
    n = len(s)
    if n == 0:
      return ""
    
    def helper(left: int, right: int, longest: str):
      if left == n:
        return longest
      
      for j in range(left, n):
        if self.isPalindrome(s[left:j+1]):
          curr_palindrome = s[left:j+1]
        
          if len(curr_palindrome) > len(longest):
            longest = curr_palindrome
            
      return helper(left+1, right, longest)
    return helper(0, n-1, "")
  
s = "babad"
# Output: "bab"
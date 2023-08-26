# Brute force
class Solution(object):
  
  def isPalindrome(self, s):
    return s == s[::-1]
  
  def longestPalindrome(self, s):
    res = ""
    l = 0
    r = len(s)-1
    
    
    for i in range(len(s)):
      for j in range(i+1, len(s) + 1):
        if self.isPalindrome(s[i:j]) and j - i > len(res):
          res = s[i:j]
    return res
            
            

  # 2 Pointer solution 
  # def  longestPalindrome2(self, s):
  #   res = ""
  #   resLen = 0
    
  #   for i in range(len(s)):
  #     # odd length
  #     l, r = i, i
  #     while l >= 0 and r < len(s) and s[l] == s[r]:
        
s = "babad"
sol = Solution()
sol.longestPalindrome(s)


class Solution(object):
  def longestPalindrome(self, s):
    res = ""
    l = 0
    r = len(s)-1
    
    for n, letter in enumerate(s):
      while l <= r:
        m = (l + r) // 2
        
        
        

s = "babad"
sol = Solution()
sol.longestPalindrome(s)


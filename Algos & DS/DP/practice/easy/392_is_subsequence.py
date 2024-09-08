class RecursiveSolution:
  def isSubsequence(self, s: str, t: str) -> bool:
    # Base cases
    if not s: # If s is empty, it's always a subsequence
      return True
    if not t: # If t is empty and s is not, s can't be a subsequence
      return False
    
    # Recursion: Compare the first character of s and t
    if s[0] == t[0]:
      # Move to the next character in both strings
      return self.isSubsequence(s[1:], t[1:])
    else:
      # Move to the next character in t but keep s unchaged
      return self.isSubsequence(s, t[1:])
  
class RecursionSolution2:
  def isSubsequence(self, s: str, t: str) -> bool:
    def helper(i: int, j: int):
      if i == len(s):
        return True
      if j == len(t):
        return False
      
      if s[i] == t[j]:
        return helper(i+1, j+1)
      else:
        return helper(i, j+1)
        
    return helper(0,0)

class Solution:
  def isSubsequence(self, s: str, t: str) -> bool:
    if len(s) == 0:
      return True
    j = 0
    
    for i in range(len(t)):
      if t[i] == s[j]:
        j += 1
      if j == len(s):
        return True
    return False
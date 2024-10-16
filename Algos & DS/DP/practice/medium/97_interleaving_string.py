# Given strings s1, s2, and s3, find whether s3 is formed by an
# interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s 
# and t are divided into n and m substrings respectively, such that:
# s = s1 + s2 + ... + sn
# t = t1 + t2 + ... + tm
# | n - m | <= 1
# The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
# Note: a + b is the concatenation of strings a and b.


class SolutionRec:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    # Base case: if the total length of s1 and s2 doesn't match s3, return False
    if len(s1) + len(s2) != len(s3):
      return False
      
    def helper(i: int, j: int, k: int) -> bool:
      # If we've reached the end of s1, s2, and s3, return True
      if i == len(s1) and j == len(s2) and k == len(s3):
        return True
      
      # If i is within bounds and s1[i] matches s3[k], recurse for the next character of s1
      if i < len(s1) and s1[i] == s3[k]:
        if helper(i+1, j, k+1):
          return True

      # If j is within bounds and s2[j] matches s3[k], recurse for the next character of s2
      if j < len(s2) and s2[j] == s3[k]:
        if helper(i, j+1, k+1):
          return True
      
      # If neither of the above conditions hold, return False
      return False
    # Start recursion with indices 0 for s1, s2, and s3
    return helper(0, 0, 0)

class SolutionMemo:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    # If we've reached the end of s1, s2, and s3, return True
    if len(s1) + len(s2) != len(s3):
      return False
    # Memoization list to store the results of subproblems
    memo = {}
    
    def helper(i: int, j: int, k: int) -> bool:
      if i == len(s1) and j == len(s2) and k == len(s3):
        return True
      
      # Try to match with s1 and recurse
      if i < len(s1) and s1[i] == s3[k] and helper(i+1, j, k+1):
        memo[(i, j)] = True
        return True
      
      # Try to match with s1 and recurse
      if j < len(s2) and s2[j] == s3[k] and helper(i, j+1, k+1):
        memo[(i, j)] = True
        return True
      
      # If neither match, memoize the result as False
      memo[(i, j)] = False
      return False
    return helper(0, 0, 0)

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
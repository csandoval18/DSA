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

class SolutionMemoHM:
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

    
class SolutionMemo:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    # Base case: Lengths of s1 and s2 combined should match s3
    if len(s1) + len(s2) != len(s3):
      return False

    # Create a memoization table dp where dp[i][j] means whether
    # s1[0:i] and s2[0:j] can form s3[0:i+j]
    dp = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    
    def helper(i: int, j: int):
      # If both s1 and s2 are exhausted, return True (base case)
      if i == 0 and j == 0:
        return True
      
      # If this subproblem has already been solved, return the stored result
      if dp[i][j] != -1:
        return dp[i][j]
      
      # Check if we can form s3 using a character from s1
      if i > 0 and s1[i - 1] == s3[i+j-1]:
        if helper(i - 1, j):
          dp[i][j] = True
          return True
      
      # Check if we can form s3 using a character from s2
      if j > 0 and s2[j - 1] == s3[i+j-1]:
        if helper(i, j - 1):
          dp[i][j] = True
          return True
      
      # If neither worked, store False in dp[i][j] and return False
      dp[i][j] = False
      return False
  
    # Call the helper function to solve the problem
    return helper(len(s1), len(s2))

class SolutionDP:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    n, m, l = len(s1), len(s2), len(s3)
    # If the total length of s1 and s2 doesn't match s3, return False immediately
    if n + m != l:
      return False
    
    # dp[i][j] will be True if s1[0:i] and s2[0:j] can interleave to form s3[0:i+j]
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    # Initialize dp[0][0], empty strings can interleave to form an empty string
    dp[0][0] = True
    
    # Fill the first row (matching s1 with the empty prefix of s2)
    for i in range(1, n + 1):
      dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
    
    # Fill the first column (matching s2 with the empty prefix of s1)
    for j in range(1, m + 1):
      dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
    
    # Fill the rest of the dp table
    for i in range(1, n + 1):
      for j in range(1, m + 1):
        # Check if the current character of s1 matches the current character of s3
        if s1[i - 1] == s3[i + j - 1]:
          dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        # Check if the current character of s2 matches the current character of s3
        if s2[j - 1] == s3[i + j - 1]:
          dp[i][j] = dp[i][j] or dp[i][j - 1]
    
    # The answer will be in dp[n][m], which tells if the whole s1 and s2 can form s3
    return dp[n][m]
        
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
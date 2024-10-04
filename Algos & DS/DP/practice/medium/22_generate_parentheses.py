from typing import List

# op = open parenthesis
# m = ds length
# ds = current string

class Solution:
  def generateParenthesis(self, n: int) -> List[str]:
    def helper(m: int, op: int, ds: str) -> None:
      if m == n*2:
        res.append(ds)
        return
      
      if op < n:
        helper(m+1, op+1, ds + "(")
      # (m - op): calculates how many closing parentheses have been used so far
      if m - op < op:
        helper(m+1, op, ds + ")")
    
    res = []
    helper(0,0,"")
    return res
    
    
class SolutionDP:
  def generateParenthesis(self, n: int) -> List[str]:
    dp = [[[] for _ in range(n+1)] for _ in range(n*2+1)]
    dp[0][0] = [""] 
    
    for m in range(n*2):
      for op in range(n+1):
        if dp[m][op]:
          if op < n:
            dp[m+1][op+1].extend([ds + "(" for ds in dp[m][op]])
          # If we can add a closing parenthesis
          if m - op < op:
            dp[m+1][op].extend([ds + ")" for ds in dp[m][op]])
    return dp[n*2][n]
            
    
class SolutionDP1:
  def generateParenthesis(self, n: int) -> List[str]:
    dp = [[] for _ in range(n+1)] # dp[i] will store all combinations for i pairs of parentheses
    dp[0] = [""] # Base case: an empty string for 0 pairs
    
    for i in range(1, n+1): # For each i pairs of parentheses
      for j in range(i):
        # Build new combinations by adding a pair of parentheses around dp[j]
        # and concatenating with dp[i-j-1]
        for first in dp[j]:
          for second in dp[i-j-1]:
            dp[i].append(f"({first}){second}")
    
    return dp[n]

n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# n = 1
# Output: ["()"]
s1 = Solution()
s2 = SolutionDP()
print(s1.generateParenthesis(n))
print(s2.generateParenthesis(n))
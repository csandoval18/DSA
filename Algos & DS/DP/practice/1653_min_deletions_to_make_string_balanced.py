# You are given a string 's' consisting only of characters 'a' and 'b'.

# You can delete any number of characters in 's' to make 's' balanced.
# 's' is balanced if there is no pair of indices (i, j) such that 
# i < j and s[i] = 'b' and s[j] = 'a'.

# Return the minimun number of deletions needed to make 's' balanced.

class Solution:
  def minimumDeletions(self, s: str) -> int:
    n = len(s)
    dp = [0] * (n+1) # Initialize a DP array where dp[i] represents the minimum deletions for s[0:i]
    count_b = 0 # Tracks number of 'b' at current index
    
    for i in range(1, n+1):
      if s[i-1] == 'a':
        dp[i] = min(dp[i-1] + 1, count_b)
      else: # s[i-1] == 'b'
        dp[i] = dp[i-1]
        count_b += 1

    return dp[n]
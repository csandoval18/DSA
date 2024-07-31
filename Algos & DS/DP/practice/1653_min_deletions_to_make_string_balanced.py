# You are given a string 's' consisting only of characters 'a' and 'b'.

# You can delete any number of characters in 's' to make 's' balanced.
# 's' is balanced if there is no pair of indices (i, j) such that 
# i < j and s[i] = 'b' and s[j] = 'a'.

# Return the minimun number of deletions needed to make 's' balanced.

# Top-down Approach:
# - We begin from n-1 instead of index 0

# For each character in s[i-1]:
# - If it is 'a', we have two choices:
#   1. Delete this 'a' to make the string balanced or keep it and ensure all previous 'b's
#   are not invalidating the balance
#   2. Keep 'a' and ensure all previous 
# - If it is 'b', we simply keep it and update the count of 'b's encountered so far

class Solution:
  def minimumDeletions(self, s: str) -> int:
    n = len(s)
    dp = [0] * (n+1) # Initialize dp arra where dp[i] represents the min deletions for s[0Li]
    count_b = 0 # To track the number of 'b' seen so far
    
    for i in range(1, n+1):
      if s[i-1] == 'a':
        dp[i] = min(dp[i-1] + 1, count_b)
      else: # s[i-1] == 'b'
        dp[i] = dp[i-1]
        count_b += 1
    
    return dp[n]

s = "aababbab"
solution = Solution()

# Bottom up approach
class Solution:
  def minimumDeletions(self, s: str) -> int:
    n = len(s)
    
    # Count total number of 'a's and 'b's in the string
    total_a = s.count('a')
    total_b = s.count('b')
    
    # Initialize left_a and right_b
    left_a = 0
    right_b = total_b
    min_deletions = min(total_a, total_b) # Initialize result to be the minimum of total 'a's or total 'b's
    
    for i in range(n):
      if s[i] == 'a':
        left_a += 1
      else:
        left_b -= 1
        
      # Calculate deletions required if we split at this point
      deletions = left_a + (total_b - right_b)
      # Update minimum deletions
      min_deletions = min(min_deletions, deletions)
      
    return min_deletions
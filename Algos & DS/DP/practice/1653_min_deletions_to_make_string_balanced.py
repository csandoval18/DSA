# You are given a string 's' consisting only of characters 'a' and 'b'.

# You can delete any number of characters in 's' to make 's' balanced.
# 's' is balanced if there is no pair of indices (i, j) such that 
# i < j and s[i] = 'b' and s[j] = 'a'.

# Return the minimun number of deletions needed to make 's' balanced.

class Solution:
  def minimumDeletions(self, s: str) -> int:
    n = len(s)
    def rec(i: int, j: int):
      if j == n-1:
        
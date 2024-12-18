'''
274. Ones and Zeroes (Medium)

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also eleme

'''

from typing import List

class Solution:
  def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    def helper(i: int, m: int, n: int) -> int:
      if i >= len(strs):
        return 0
      if m == 0 and n == 0:
        return 0
      
      zeroes = strs.count('0')
      ones = strs.count('1')
      new_m, new_n = m - zeroes, n - ones
      
      # If idx is not exhausted and new m and n values are non negative
      take, skip = 0, 0
      if i < len(strs) and new_m >= 0 and new_n >= 0:
        take = 1 + helper(i+1, new_m, new_n) # Then add 1 and return
      else: # Skip current string
        skip = helper(i+1, m, n)
        
      return min(take, skip)
    
        

strs = ["10","0001","111001","1","0"]
m = 5
n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
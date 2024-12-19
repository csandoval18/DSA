'''
274. Ones and Zeroes (Medium)

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also eleme

'''

from typing import List

class SolutionRec:
  def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    def helper(i: int, m: int, n: int) -> int:
      if i >= len(strs):
        return 0
      if m == 0 and n == 0:
        return 0
      
      zeroes = strs[i].count('0')
      ones = strs[i].count('1')
      
      skip = helper(i+1, m, n)
      
      take = 0
      if m >= zeroes and n >= ones:
        take = 1 + helper(i+1, m - zeroes, n - ones)
        
      return max(take, skip)
    return helper(0, m, n)


class SolutionMemo:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
      memo = {}

      def helper(i: int, m: int, n: int) -> int:
        if i >= len(strs):
          return 0

        if (i, m, n) in memo:
          return memo[(i, m, n)]

        zeroes = strs[i].count('0')
        ones = strs[i].count('1')

        skip = helper(i+1, m, n)
        take = 0
        if m >= zeroes and n >= ones:
          take = 1 + helper(i+1, m - zeroes, n - ones)

        memo[(i, m, n)] = max(take, skip)
        return memo[(i, m, n)]
      return helper(0, m, n)
        

class SolutionDP:
  def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
    # Initialize the DP table
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    # Process each string in strs
    for s in strs:
      zeroes = s.count('0')
      ones = s.count('1')
      
      # Update the DP table in reverse to prevent overwriting
      for i in range(m, zeroes -1, -1):
        for j in range(n, ones - 1, -1):
          dp[i][j] = max(dp[i][j], 1 + dp[i - zeroes][j - ones])
    
    # The answer is dp[m][n]
    return dp[m][n]


strs = ["10","0001","111001","1","0"]
m = 5
n = 3
# Output: 4
# Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
# Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
# {"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.
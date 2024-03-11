from typing import List

# Printing the LIS

# In order to print the LIS, we maintain a separate array along with a dp array (hash)
# Whenever we update our dp[i] value in the inner loop, we know that for index i,
# the previous index is prev_index. 

nums = [10,9,2,5,3,7,101,18]

# Traceback LIS
# Print LIS

def lengthofLIS(nums: List[int]) -> int:
  n = len(nums)
  dp = [1]*n
  maxIndex = 1
  _hash = [0]*n
  last_index = 0
  
  for i in range(n):
    _hash = i
    for prev in range(i):
      if nums[prev] < nums[i] and 1 + dp[prev] > dp[i]:
        dp[i] = 1 + dp[prev]
        _hash[i] = prev
  return max(dp)
from typing import List

# 673. Number of Longest Increasing Subsequences

def findNumberOfLIS(nums: List[int]) -> int:
  n = len(nums)
  dp = [1]*n
  count = [1]*n
  mLength = 1
  
  for i in range(n):
    for prev in range(i):
      if nums[prev] < nums[i] and 1+dp[prev] >  dp[i]:
        dp[i] = 1 + dp[prev]
        count[i] = count[prev]
      
      elif nums[prev] < nums[i] and 1+dp[prev] == dp[i]:
        # Increase the count
        count[i] += count[prev]
    mLength = max(mLength, dp[i])
    
  LIS_cnt = 0
  for i in range(n):
    if dp[i] == mLength:
      LIS_cnt += count[i]
      
  return LIS_cnt

# nums = [1,3,5,4,7]
nums = [1, 5, 4, 3, 2, 6, 7, 2]

print(findNumberOfLIS(nums))
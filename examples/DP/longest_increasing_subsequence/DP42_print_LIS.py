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
  # Array to store length of the LIS ending at i
  dp = [1]*n
  # Array to store the predecessor of each element in the LIS
  
  
    
  return max(dp)
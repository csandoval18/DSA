from typing import List

# Printing the LIS

# In order to print the LIS, we maintain a separate array along with a dp array (prev)
# Whenever we update our dp[i] value in the inner loop, we know that for index i,
# the previous index is prev_index. 


# Traceback Print LIS

def lengthOfLIS(nums: List[int]) -> int:
  n = len(nums)
  dp = [1]*n
  
  for i in range(1, n):
    for prev in range(i):
      if nums[prev] < nums[i]:
        dp[i] = max(dp[i], 1 + dp[prev])
  
  return max(dp)
  
  
def longestIncreasingSubsequence(arr, n):
  dp = [1] * n
  hash = list(range(n))

  for i in range(1, n):
    for prev_index in range(i):
      # We add the condition "1 + dp[prev_index] > dp[i]:" to ensure that we are updating dp[i] only if the length of the subsequence
      # ending at arr[i] is strickly greater than the length of the subsequence ending at "1 + arr[prev_index]"
      
      # The added condition basically checks if we add the arr[i] to the subsequence length at prev (hence incrementing by 1) is bigger 
      # than the subsequence at the current cell dp[i]
      if arr[prev_index] < arr[i] and 1 + dp[prev_index] > dp[i]:
        dp[i] = 1 + dp[prev_index] # Update dp[i] to the new longer length
        hash[i] = prev_index # Update the hash to keep track of the subsequence previous_index of the ith element

  ans = -1
  lastIndex = -1

  for i in range(n):
    if dp[i] > ans:
      ans = dp[i]
      lastIndex = i

  temp = [arr[lastIndex]]

  while hash[lastIndex] != lastIndex:
    lastIndex = hash[lastIndex]
    temp.append(arr[lastIndex])

  temp.reverse()
  print("The subsequence elements are", end=" ")
  for i in range(len(temp)):
    print(temp[i], end=" ")
  print()

  return ans

    
# Chatgpt
def printLIS(nums: List[int]) -> int:
  n = len(nums)
  # Array to store length of the LIS ending at i
  dp = [1]*n
  # Array to store the predecessor of each element in the LIS
  prev = [-1]*n
  
  # Fill dp[] such that dp[i] contains the length of the LIS ending at arr[i]
  # i = current index | j = previous index
  for i in range(1, n):
    for j in range(i):
      if nums[j] < nums[i] and dp[i] < 1 + dp[j]:
        dp[i] = 1 + dp[j]
        prev[i] = j
  
  # Find the index of the max value in dp[]
  lis_length = max(dp)
  lis_index = dp.idndex(lis_length)
  
  # Reconstruct the LIS
  LIS = []
  while lis_index != -1:
    LIS.append(nums[lis_index])
    lis_index  = prev[lis_index]
  
  # Since we reconstructed it backwards, reverse it
  LIS.reverse()
  return LIS
nums = [10,9,2,5,3,7,101,18]
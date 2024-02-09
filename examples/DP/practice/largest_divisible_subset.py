from typing import List

# Given a set of distinct positive integers nums, 
# return the largest subset answer such that every 
# pair (answer[i], answer[j]) of elements in this subset satisfies:

# 1. answer[i] % answer[j] == 0, or
# 2. answer[j] % answer[i] == 0

def largestDivisibleSubset(nums: List[int]) -> List[int]:
  # If nums is empty we can return an empty res arr
  if not nums:
    return []
  
  # 1. Sort nums arr
  nums.sort()
  n = len(nums)
  # 2. Initialize arr with every starting possible index [[1], [2], [3]]
  dp = [[nums[i]] for i in range(n)]
  print("dp:", dp)
  max_len =  1
  max_ss_idx = 0
  
  for i in range(1, n):
    # Inner for loop traverses range(j < i) to check if all the previous nums values of the subset meet the conditions given 
    # with the current value nums[i]
    for j in range(i):
      print("i:", i)
      print("j:", j)
      print("dp:", dp)
      # The len(dp[i]) < len(dp[j]) + 1 condition is used to determine whether appending `nums[i]` to the ss endingat `nums[j]`
      # will result in a larger ss than the one currently ending at `nums[i]`
      
      # dp[i] represents the largest divisible subset ending at nums[i].
      # dp[j] represents the largest divisible subset ending at nums[j], where j < i.
      # If nums[i] is divisible by nums[j], it means that we can potentially extend the subset ending at nums[j] by adding nums[i].
      # However, we only append nums[i] to the subset ending at nums[j] if doing so results in a larger subset than the one currently ending at nums[i].
      
      # Basically it checks the new max subset is larger than the prev
      if nums[i] % nums[j] == 0 and len(dp[i]) < len(dp[j]) + 1:
        # then you append the num[i] to the arr in dp[i] which holds dp[j]
        dp[i] = dp[j] + [nums[i]]
        if len(dp[i]) > max_len:
          max_len = len(dp[i])
          max_ss_idx = i
    print()
          
  return dp[max_ss_idx]   

nums = [1,2,3]
print(largestDivisibleSubset(nums))
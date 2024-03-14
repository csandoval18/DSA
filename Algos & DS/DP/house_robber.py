from typing import List

def rob(nums):
  n = len(nums)
  
  def helper(arr):
    prev = arr[0]
    prev2 = 0

    for i in range(1, len(arr)):
      pick = arr[i]
      if i > 1:
        pick += prev2
      nonPick = prev

      cur_i = max(pick, nonPick)
      print("i:", i, "pick:", pick, "nonPick:", nonPick, "cur_i:", cur_i)  # Add this line for debugging
      prev2 = prev
      prev = cur_i

    return prev
    
  arr1 = []
  arr2 = []

  if n == 1:
    return nums[0]

  for i in range(n):
    if i != 0:
      arr1.append(nums[i])
    if i != n - 1:
      arr2.append(nums[i])

  ans1 = helper(arr1)
  ans2 = helper(arr2)

  print("Intermediate results:")
  print("arr1:", arr1, "max loot:", ans1)
  print("arr2:", arr2, "max loot:", ans2)
  return max(ans1, ans2)

nums = [1,5,1,2,6]
print(rob(nums))

# def robFixAttempt(nums: List[int]) -> int:
#   def solve(arr):
#     n = len(arr)
#     prev = arr[1]  # Start from the loot of the first house
#     prev2 = arr[0]  # Start from the loot of the second house

#     for i in range(2, n):  # Start from the third house
#       pick = arr[i] + prev2
#       nonPick = prev

#       cur_i = max(pick, nonPick)
#       prev2 = prev
#       prev = cur_i

#     return prev

#   n = len(nums)
#   # No need to split nums into arr1 and arr2, just pass nums directly to solve function
#   if n == 1:
#     return nums[0]
    
#   # Calculate maximum loot for arr1 including the first house
#   max_loot1 = solve(nums[2:]) + nums[0] if n > 2 else nums[0]
#   # Calculate maximum loot for arr2 including the last house
#   max_loot2 = solve(nums[1:-1])


#   # Return the maximum of max_loot1 and max_loot2
#   return max(max_loot1, max_loot2)
  
# print(robFixAttempt(nums))


def rob(self, nums: List[int]) -> int:
  if not nums:
    return 0

  n = len(nums)
  if n == 1:
    return nums[0]

  dp = [0] * n
  dp[0] = nums[0]
  dp[1] = max(nums[0], nums[1])

  for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2] + nums[i])

  return dp[-1]


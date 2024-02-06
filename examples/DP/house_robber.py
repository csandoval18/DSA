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
      nonPick = 0 + prev

      cur_max = max(pick, nonPick)
      prev2 = prev
      prev = cur_max

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

  return max(ans1, ans2)

nums = [1,5,1,2,6]
print(rob(nums))
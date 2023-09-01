# Does not pass last test with large array in lc 
def rotateAttempt(nums, k):
  tmp = 0
  for i in range(k):
    tmp = nums.pop(-1)
    nums.insert(0, tmp)
  return nums

# Solution
def rotate(nums, k):
  # Handles cases where k > len(nums)
  k = k % len(nums)
  # Reverse the entire array
  nums.reverse()
  # Reverse the first k elements
  nums[:k] = reversed(nums[:k])
  # Reverse the remaining elements
  nums[k:] = reversed(nums[k:])
  
# nums = [1,2,3,4,5,6,7]
nums = [-1,-100,3,99]
print(rotate(nums, 2))
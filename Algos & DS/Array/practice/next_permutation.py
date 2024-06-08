def nextPermutation(nums):
  n = len(nums)
  sep = -1
  
  for i in range(n-2, -1, -1):
    if nums[i] < nums[i+1]:
      sep = i
      break
  
  if sep == -1:
    nums.sort()
    return nums
  
  for i in range(n-1, sep, -1):
    if nums[i] > nums[sep]:
      nums[i], nums[sep] = nums[sep], nums[i]
      break
  
  nums[sep+1:] = reversed(nums[sep+1:])
  return nums
def findPeakElement(nums: [int]) -> int:
  n = len(nums)
  if n == 1:
    return 0
  elif nums[0] > nums[1]:
    return 0
  elif nums[n-1] > nums[n-2]:
    return n-1
  
  l, r = 1, n-2
  
  while l<=r:
    m = (l+r)//2
    
    if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
      return m
    elif nums[m-1] < nums[m]:
      l = m+1
    else:
      r = m-1
  return -1


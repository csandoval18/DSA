def findMin(nums):
  l = 0
  r = len(nums) - 1
  minVal = float('-inf')
  
  while l <= r:
    m = (l+r) // 2
    
    # Find section with sorted half
    if nums[l] <= nums[m]:
      # Find min of the sorted left section
      minVal = min(minVal, nums[l])
      l = m+1
    elif nums[m] <= nums[r]:
      # Find min in sorted right section
      minVal = min(minVal, nums[m])
      r = m-1
      
  return minVal
def search(nums, target):
  l = 0
  r = len(nums)-1
  
  while l <= r:
    m = (l+r) // 2
    
    if nums[m] == target:
      return m
    
    # Find sorted half
    if nums[l] <= nums[m]:
      if nums[l] <= target and target <= nums[m]:
        r = m-1
      else:
        l = m+1
    if nums[m] <= nums[r]:
      if nums[m] <= target and target <= nums[r]:
        l = m+1
      else:
        r = m-1 
        
  return -1
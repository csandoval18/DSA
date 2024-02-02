def search(nums, target):
  l = 0
  r = len(nums)-1
  
  while l <= r:
    m = (l+r) // 2
    
    # Base case
    if nums[m] == target:
      return m
    
    # Check if left half is sorted
    if nums[l] <= nums[m]:
      # Check if target is within left sorted half
      if nums[l] <= target and target <= nums[m]:
        r = m - 1
      # Else target could be in right non-sorted side
      else:
        l = m + 1
    elif nums[m] <= nums[r]:
      # Check if target is within right sorted half
      if nums[m] <= target and target <= nums[r]:
        l = m + 1
      # Else target could be in left non-sorted half
      else:
        r = m - 1
        
  return -1     
    
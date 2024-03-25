def search(nums, target):
  l = 0
  r = len(nums)-1
  
  while l <= r:
    m = (l+r) // 2
    
    if nums[m] == target:
      return True
    
    # Handles case where nums[l], nums[m], and nums[r] are the same value 
    # and sorted section can not be determined
    elif nums[l] == nums[m] and nums[m] == nums[r]:
      l += 1
      r -= 1
      
    elif nums[l] <= nums[m]:
      if nums[l] <= target and target <= nums[m]:
        r = m-1
      else:
        l = m+1
    elif nums[m] <= nums[r]:
      if nums[m] <= target and target <= nums[r]:
        l = m+1
      else:
        r = m-1
        
  return False
  
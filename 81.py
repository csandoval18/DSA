def search(nums, target):
  l = 0
  r = len(nums)-1
  
  while l <= r:
    m = (l+r) // 2
    
    if nums[m] == target:
      return True
      
    elif nums[l] == nums[m] and nums[m] == nums[r]:
      l = l+1
      r = r-1
    
    if nums[l] <= nums[m]:
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

# [1,0,1,1,1]
#  L   M   R
# nums = [2,4,5,0,0,1,2]
nums = [1,0,1,1,1]
target = 0

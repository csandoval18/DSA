def search(nums: [int], target: int) -> int:
  n = len(nums)
  l, r = 0, n-1
  
  while l<=r:
    m = (l+r)//2
    
    # Base caser
    if nums[m] == target:
      return m
      
    # Check if left half is sorted
    if nums[l] <=  nums[m]:
      if nums[l] <= target <= nums[m]:
        r = m-1
      else:
        l = m+1
    # Check if right side is sorted
    elif nums[m] <= nums[r]:
      if nums[m] <= target <= nums[r]:
        l = m+1
      else:
        r = m-1
  return -1
      
    
    
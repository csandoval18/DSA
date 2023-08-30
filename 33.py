def search(nums, target):
  l = 0
  r = len(nums)-1
  
  while l <= r:
    m = (l+r) // 2
    
    # base case
    if nums[m] == target:
      return m
      
    
  

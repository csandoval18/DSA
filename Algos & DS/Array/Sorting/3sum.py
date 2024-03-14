def threeSum(nums):
  n = len(nums)
  nums.sort()
  res = []
  
  for i in range(n):
    if i != 0 and nums[i] == nums[i-1]:
      continue
    
    j = i+1
    k = n-1
    
    while j < k:
      total_sum = nums[i] + nums[j] + nums[k]
      
      if total_sum < 0:
        j += 1
      elif total_sum > 0:
        k -= 1
      else:
        res.append([nums[i], nums[j], nums[k]])
        j += 1
        k -= 1
        # Not necessary (skips duplicates of j and k pointers)
        while j<k and nums[j] == nums[j-1]:
          j += 1
        while j<k and nums[k] == nums[k+1]:
          k -= 1
  return res
      
      
      
      
        
      
    
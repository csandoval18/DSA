def threeSum(nums):
  n = len(nums)
  res = []
  nums.sort()
  
  for i in range(n):
    if i != 0 and nums[i] == nums[i-1]: 
      continue
    
    j = i+1
    k = n-1
    
    while j < k:
      tmp = nums[i] + nums[j] + nums[k]
      
      if tmp < 0:
        j += 1
      elif tmp > 0:
        k -= 1
      else:
        res.append([nums[i], nums[j], nums[k]])
        j += 1
        k -= 1
        
  return res


# This one adds extra while loops when target is met to skip j and k duplicates and not just i 
def threeSumMoreOptimized(nums):
  n = len(nums)
  res = []
  nums.sort()
  
  for i in range(n):
    if i != 0 and nums[i] == nums[i-1]: 
      continue
    
    j = i+1
    k = n-1
    
    while j < k:
      tmp = nums[i] + nums[j] + nums[k]
      
      if tmp < 0:
        j += 1
      elif tmp > 0:
        k -= 1
      else:
        res.append([nums[i], nums[j], nums[k]])
        j += 1
        k -= 1
        
        while j < k and nums[j] == nums[j-1]:
          j += 1
        while j < k and nums[k] == nums[k+1]:
          k -= 1
        
  return res
        

nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

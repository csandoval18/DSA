def fourSum(nums, target):
  # 4 Sum
  n = len(nums)
  nums.sort()
  res = []
  
  for i in range(n):
    if i != 0 and nums[i] == nums[i-1]:
      continue
    
    for j in range(i+1, n):
      if j != i+1 and nums[j] == nums[j-1]:
        continue
      
      k = j+1
      l = n-1
      
      while k < l:
        curr_sum = nums[i] + nums[j] + nums[k] + nums[l]
        
        if curr_sum < target:
          k += 1 
        elif curr_sum > target:
          l -= 1
        else:
          res.append([nums[i], nums[j], nums[k], nums[l]])
          k += 1
          l -= 1
    return res
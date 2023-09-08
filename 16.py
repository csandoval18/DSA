def threeSumClosest(nums, target):
  n = len(nums)
  res = 0
  nums.sort()
  
  for i in range(n):
    if i != 0 and nums[i-1] == nums[i]:
      continue
    
    j = i+1
    k = n-1
    
    while j < k:
      curr_sum = nums[i] + nums[j] + nums[k]
      
      if curr_sum < 0:
        j += 1
      elif curr_sum > 0:
        k -= 1
      else:
        tmp = [nums[i], nums[j], nums[k]]
        res.append(tmp)
        j += 1
        k -= 1
      
        while j < k and nums[j-1] ==  nums[j]:
          j += 1 
        while j < k and nums[k] == nums[k+1]:
          k -= 1
        
  return res

nums = [-1,0,1,2,-1,4]
# nums = [0,1,1]
# nums = [0,0,0]

print(threeSumClosest(nums))
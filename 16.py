def threeSumClosest(nums, target):
  n = len(nums)
  res = 0
  min_dist = float('inf')
  nums.sort()
  
  for i in range(n):
    if i != 0 and nums[i-1] == nums[i]:
      continue
    
    j = i+1
    k = n-1
    
    while j < k:
      curr_sum = nums[i] + nums[j] + nums[k]
      dist_to_target = abs(target - curr_sum)
      
      if dist_to_target < min_dist:
        min_dist = dist_to_target
        res = curr_sum
      
      
      if curr_sum < target:
        j += 1
      elif curr_sum > target:
        k -= 1
      else:
        j += 1
        k -= 1
      
        while j < k and nums[j-1] ==  nums[j]:
          j += 1 
        while j < k and nums[k] == nums[k+1]:
          k -= 1
        
  return res

# nums = [-1,2,1,-4]
# target = 1
# [-4,-1,1,2]
# nums = [0,0,0]
nums = [1,1,1,0]
target = -100

print(threeSumClosest(nums, target))
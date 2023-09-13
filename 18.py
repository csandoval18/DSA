# Brute force
def fourSum(nums, target):
  n = len(nums)
  res = []
  
  for i in range(n-3):
    if i != 0 and nums[i] != nums[j]:
      continue
      
    for j in range(i+1, n-2): 
      if j != i+1 and nums[j] == nums[j-1]:
        continue
      
      k =j+1
      l = n-1
      
      while k < l:
        curr_sum = nums[i] + nums[j] + nums[k] + nums[l]
        
        if curr_sum < 0:
          k += 1
        elif curr_sum > 0:
          l -= 1
        else:
          res.append([nums[i], nums[j], nums[k], nums[l]])
          k += 1
          l -= 1
          
  return res

nums = [1,0,-1,0,-2,2] 
target = 0

print(fourSum(nums, target))
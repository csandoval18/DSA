def rearrangeArray(nums):
  n = len(nums)
  res = [0] * n
  posIndex = 0 
  negIndex = 1
  
  for i in range(n):
    if nums[i] < 0:
      res[negIndex] = nums[i] 
      negIndex += 2
    else:
      res[posIndex] = nums[i]
      posIndex += 2
  return res
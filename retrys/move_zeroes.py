def moveZeroes(nums):
  count = 0
  i = 0
  
  while i != len(nums):
    print("i:", i)
    if nums[i] == 0:
      nums.pop(i)
      count += 1
      i -= 1
    i += 1
    
  for i in range(count):
    nums.append(0)
  
  return nums

# nums = [0,1,0,3,12]
nums = [0,0,1]
print(moveZeroes(nums))
      
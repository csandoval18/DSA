def nextPermutation(nums):
  n = len(nums)
  sep = -1
  
  # 2 pointers to compare so start at n-2 and compare to n-1
  for i in range(n-2, -1, -1):
    if nums[i] < nums[i+1]:
      sep = i
      break
    
  if sep == -1:
    nums.reverse()
    return nums
  
  for i in range(n-1, sep-1, -1):
    if nums[i] > nums[sep]:
      nums[i], nums[sep] = nums[sep], nums[i]
      break
  
  # reverses right section with
  nums[sep+1:] = reversed(nums[sep+1:])
  return nums

# nums = [1,2,3]
nums = [3,2,1]
# nums = [5,3,4,3,2,1]
print(nextPermutation(nums))
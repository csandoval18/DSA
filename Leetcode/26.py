# Works but leetcode does not accept it
def removeDuplicates(nums):
  n = len(nums)
  r = 1
  l = 0
  while(r != n-1):
    if nums[l] == nums[r]:
      nums.pop(r)
    else:
      r += 1
      l += 1
  return nums

nums = [1,1,2]
print(removeDuplicates(nums))

# Chatgpt solution
def remove_duplicates(nums):
  # Empty array
  if not nums:
    return 0
  
  print("l:", l)
  print("r:", r)
  print("n:", )
  
  l = 0
  
  for r in range(1, len(nums)):
    if nums[l] != nums[r]:
      l += 1
      nums[l] = nums[r]
      
  return l + 1
      
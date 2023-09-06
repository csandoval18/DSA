# O(n + (count of 0's))
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


# O(n)
def moveZeroesOptimal(nums): 
  l = 0
  
  for r, n in enumerate(nums):
    print("l:", l)
    print("r:", r)
    if n != 0:
      nums.insert(l, nums[r])
      print("nums:", nums)
      print("nums[l]:", nums[l])
      print("nums[r]:", nums[r])
      nums.pop(r+1)
      l += 1
    print("\n")
  return nums
    
      
nums = [0,1,0,3,12]
# nums = [0,0,1]
print(moveZeroesOptimal(nums))
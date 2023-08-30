def findMin(nums):
  l = 0
  r = len(nums)-1
  
  while l <= r:
    print("l:", l)
    print("r:", r)
    m = (l + r) // 2
    print("m:", m)
    print("\n")
    
    if nums[l] > nums[r]:
      l = m
    elif nums[l] < nums[r]:
      r = m
      
    if r-l == 1:
      return min(nums[l], nums[r])
    

# nums = [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
# nums = [11,13,15,17]
# nums = [2,3,1]
print(findMin(nums))
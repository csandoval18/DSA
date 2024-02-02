def findMinBruteForce(nums):
  minVal = float('inf')
  for n in nums:
    if n < minVal:
      minVal = n
  return minVal

def findMinAttempt(nums):
  l = 0
  r = len(nums)-1
  
  while l <= r:
    m = (l + r) // 2
    
    if nums[l] > nums[r] and nums[m-1] > nums[m]:
      l = m
    elif nums[l] < nums[r]:
      r = m
      
    if r-l == 1:
      return min(nums[l], nums[r])
    

# nums = [3,4,5,1,2]
# nums = [4,5,6,7,0,1,2]
# nums = [11,13,15,17]
# nums = [2,3,1]

# This case breaks previous algo without "and nums[m-1] > nums[m]"
#         L   M   R
# nums = [5,1,2,3,4]

#             L   R
# nums = [5,1,2,3,4]

# //////////////////////////////////////////////////////

def findMin(nums):
  minVal =  float('inf')
  l, r = 0, len(nums)-1
  
  while l <= r:
    m = (l+r) // 2
    
    # Get min in sorted half
    if nums[l] <= nums[m]: 
        minVal = min(minVal, nums[l])
        l = m + 1
    elif nums[m] <= nums[r]: 
        minVal = min(minVal, nums[m])
        r = m - 1
        
  return minVal
    
    # Perform binary search in non sorted half
    
    
    
      

# print(findMin(nums))
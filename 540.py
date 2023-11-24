def singleNonDuplicate(nums: [int]) -> int:
  n = len(nums)
  
  # If only 1 element in arr return 
  if n == 1:
    return nums[0]
  # Check if first el is unique  
  elif nums[0] != nums[1]:
    return nums[0]
  # Check if last el is unique  
  elif nums[n-1] != nums[n-2]:
    return nums[n-1]
  l = 1
  r = n-2
  
  while l<=r:
    m = (l+r)//2
    
    # If nums[m] is the single el
    if nums[m] != nums[m+1] and nums[m] != nums[m-1]:
      return nums[m]
    # We are in the left
    elif (m%2 == 1 and nums[m] == nums[m-1]) or (m%2 == 0 and nums[m] == nums[m+1]):
      l = m+1
    # We are in the right:
    else:
      # Eliminate the right half
      r = m-1
  return -1
  
  
# [1,1,2,3,3,4,4,8.8]
#  L       M       R

#  0 1 2 3 4 5 6 7 8
# [1,1,2,3,3,4,4,8,8]
#  L       M       R
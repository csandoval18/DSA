# Pivot Index

# Given an arr of int nums, calc the pivot index of this arr.

# The pivot index is the index where the sum of all the nums strickly to the left of the
# index is equal to the sum of all the nms strickly to the  index's right

# If the index is on the left edge of the arr, then the left sum is 0 because there are 
# no elements to the left. This also applies to the right edge of the arr.

# Return the leftmost pivot index. If no such index exists return -1

# O(2n) n for getting suffix sum and another n for finding pivot point
def pivotIndex(nums: [int]) -> int:
  n = len(nums)
  suffix_sum = sum(nums)
  prefix_sum = 0
  
  for i in range(n):
    suffix_sum -= nums[i]
    
    if suffix_sum == prefix_sum:
      return i
    
    prefix_sum += nums[i]
    
  return -1 # If no pivot index is found
  
  
    
    
    
    
    
  
    
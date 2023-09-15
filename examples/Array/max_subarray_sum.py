# Brute Force O(n^3)

def max_subarray_sum_brute_force(nums):
  max_sum = float('-inf')
  n = len(nums)
  
  for i in range(n):
    for j in range(i, n):
      curr_sum = 0
      for k in range(i, j+1):
        curr_sum = nums[k]
      max_sum = max(max_sum, curr_sum)

  return max_sum


# Sliding Window O(n)

def max_subarray_sum_sliding_window(nums):
  if not nums:
    return 0
  
  max_sum = float('-inf')
  curr_sum = 0
  left = 0
  
  for right in range(len(nums)):
    curr_sum += nums[right]
    max_sum = max(max_sum, curr_sum)
    
    # If the curr_sum become negative, reset it and move left pointer
    if curr_sum < 0:
      curr_sum = 0
      left = right+1
      
  return max_sum
    
  
# nums [1,2,3,4,5]

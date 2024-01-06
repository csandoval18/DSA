def lengthOfLIS(nums: [int]) -> int:
  # def util(i, prev_idx, arr, n):
    # if i == n: 
    #   return 0
    
    # length = 0+util(i+1, prev_idx, arr, n)
    # if (prev_idx == -1 or arr[i] > arr[prev_idx]):
    #   length = max(length, 1+util(i+1, i, arr, n))
    
    # return length
  
  n = len(nums)
  LIS = [1] * n
  
  for i in range(n-1,-1,-1):
    for j in range(i+1, n):
      if nums[i] < nums[j]:
        LIS[i] = max(LIS[i], 1+LIS[j])

  return max(LIS)
  
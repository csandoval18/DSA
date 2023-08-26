def maxSubarraySum(arr, k):
  max_sum = float('-inf')
  
  # Calc initial window sum
  window_sum = sum(arr[:k]) 
  
  for i in range(k, len(arr)):
    # Update window sum
    window_sum += arr[i] - arr[i-k]
    
    # Update max sum
    max_sum = max(max_sum, window_sum)
    
  return max_sum
    
arr = [2,1,5,1,3,2]   
k = 3
print(maxSubarraySum(arr, k))
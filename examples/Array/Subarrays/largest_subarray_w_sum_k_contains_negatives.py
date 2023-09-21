# Chatgpt
def largestSubarraySum(nums, k):
    max_length = 0
    current_sum = 0
    sum_to_index = {0: -1}  # Initialize with a sum of 0 at index -1

    for i in range(len(nums)):
        current_sum += nums[i]

        # If the (current_sum - k) exists in sum_to_index, it means we found a subarray with sum k.
        if current_sum - k in sum_to_index:
            max_length = max(max_length, i - sum_to_index[current_sum - k])

        # If the current_sum is not in sum_to_index, store it with its index.
        if current_sum not in sum_to_index:
            sum_to_index[current_sum] = i

    return max_length
    
    


def longestSubarrayWithSumk(nums: [int], k: int) -> int:
  hm = {}
  maxLen = 0
  curr_sum = 0
  
  for i in range(len(nums)):
    curr_sum += nums[i]
    
    if curr_sum == k:
      maxLen = max(maxLen, i+1)
    
    rem = curr_sum - k
    
    if rem in hm:  
      leng = i - hm[rem]
      maxLen = max(maxLen, leng)
      
    # Need to add this condition to make it work with 0s and avoid updating index in hm
    # with 0 value at indexes
    if curr_sum not in hm:
      hm[curr_sum] = i
      
  return maxLen
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
    
    
    
# Strivers 2 pointer approach # Works w/ negatives
def getLongestSubarray(nums: [int], k: int) -> int:
    # Write your code here
    left = 0
    right = 0
    currSum = 0
    maxLen = 0

    while right < len(nums):
        # For case when currSum > k and we must decrement to reach k or a 
        # number below k. Make sure left <= right
        while left <= right and currSum > k:
            currSum -= nums[left]
            left += 1

        # If sum of k found, then that means there is a subarray with sum 6
        # between range(left, right+1)
        if currSum == k:
            maxLen = max(maxLen, right-left+1)
        
        right += 1

        if right < len(nums):
            currSum += nums[right]

    return maxLen
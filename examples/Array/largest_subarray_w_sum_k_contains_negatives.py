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


      
    
# Observations:
# remember there can not be a length greater than k.
# Ex: k = 3, arr = [1,1,1] 


# Brute force not optimal O(n^2) there is also a O(n^3) with k->j+1
def longestSubarrayWithSumK(a: [int], k: int) -> int:
  n = len(a)
  max_len = float('-inf')
  
  for i in range(n):
    print("i:" ,i)
    curr_sum = 0
    for j in range(i,n):
      print("j:" ,j)
      curr_sum += a[j]
      print("curr sum:", curr_sum)
      if curr_sum == k:
        max_len = max(max_len, (j+1)-(i+1))
  
  return max_len



# O(n) Using hm
def longestSubarrayWithSumk(a: [int], k: int) -> int:
  hm = {}
  maxLen = 0
  curr_sum = 0
  
  for i in range(len(a)):
    curr_sum += a[i]
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
    

# O(2N) w/ 2 pointers approach
def getLongestSubarray(nums: [int], k: int) -> int:
  # Write your code here
  left = 0
  right = 0
  currSum = 0
  maxLen = 0

  while right < len(nums):
    currSum += nums[right]
    # For case when currSum > k and we must decrement to reach k or a 
    # number below k. Make sure left <= right
    while left <= right and currSum > k:
      currSum -= nums[left]
      left += 1

    # If sum of k found, then that means there is a subarray with sum 6
    # between range(left, right+1)
    if currSum == k:
      maxLen = max(maxLen, right-left+1)
    
    # Increase right to next element and add element value
    right += 1

  return maxLen
    
a = [1,2,3,1,1,1,1]
# a = [2,2,4,1,2]
k = 3
print(longestSubarrayWithSumK(a, k))
      

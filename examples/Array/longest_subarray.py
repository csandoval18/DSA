# Find longest subarray, totally useless, the longest len subarray = len(array)
def longestSubarray(a: [int]) -> int:
  max_len = 0
  n = len(a)
  
  for i in range(n):
    for j in range(i,n):
      subarr_len = (j-i) + 1 # + 1 to remove 0 index start   
      max_len = max(max_len, subarr_len)
  return max_len
      
      
nums = [1,2,3,4,5]
# print(longestSubarray(nums))
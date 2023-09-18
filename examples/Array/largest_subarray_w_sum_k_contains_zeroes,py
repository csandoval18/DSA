# Observations:
# remember there can not be a length greater than k.
# Ex: k = 3, arr = [1,1,1] 


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

def longestSubarrayWithSumk(a: [int], k: int) -> int:
  preSumMap = {}
  maxLen = 0
  curr_sum = 0
  
  for i in range(len(a)):
    curr_sum += a[i]
    if curr_sum == k:
      maxLen = max(maxLen, i+1)
    
    rem = curr_sum - k
    if rem in preSumMap:  
      leng = i - preSumMap[rem]
      maxLen = max(maxLen, leng)
      
    # Need to add this condition to make it work with 0s and avoid updating index in hm
    # with 0 value at indexes
    if curr_sum not in preSumMap:
      preSumMap[curr_sum] = i
  return maxLen
    

      
a = [1,2,3,1,1,1,1]
# a = [2,2,4,1,2]
k = 3
print(longestSubarrayWithSumK(a, k))
      

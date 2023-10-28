# Longest Subarray With Zero Sum

# Brute Force 
def getLongestZeroSumSubarraLengthBF(arr: [int]) -> int:
  n = len(arr)
  longest = 0
  
  for i in range(n):
    for j in range(i, n):
      curr_sum = 0
      for k in range(i, j+1):
        curr_sum += arr[k]
      if curr_sum == 0:
        longest = max(longest, j-i+1)
  return longest
  
# Better  
def getLongestZeroSumSubarraLength(arr: [int]) -> int:
  n = len(arr)
  longest = 0
  
  for i in range(n):
    curr_sum = 0
    for j in range(i, n):
      curr_sum += arr[j]
      if curr_sum == 0:
        longest = max(longest, j-i+1)
  return longest
  

# Optimal
def getLongestZeroSumSubarrayLength(arr):
  n = len(arr)
  longest = 0
  curr_sum = 0
  hm = {}
  
  for i in range(n):
    curr_sum += arr[i]
    if sum == 0:
      longest = i+1
    else:
      if curr_sum in hm:
        longest = max(longest, i-hm[curr_sum])
      else:
        hm[curr_sum] = i
  return longest
  
arr = [1,0,-1,1] 
print(getLongestZeroSumSubarraLength(arr))
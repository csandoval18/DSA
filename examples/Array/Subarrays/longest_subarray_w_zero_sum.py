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
  
arr = [1,0,-1,1] 
print(getLongestZeroSumSubarraLength(arr))

# Optimal
def getLongestZeroSumSubarrayLength(arr):
  longest = 0
  hm = {}
  
  for i in range(n):
    
 
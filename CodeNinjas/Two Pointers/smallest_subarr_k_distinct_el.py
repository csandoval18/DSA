# So this is a subarray problem, then best case is O(n) linear time
# Brute force solutions would be O(n^3) and O(n^2) with nested loops

# These solutions work but codeninjas doesn't accept them due to their shitty testcases

# BF
def smallestSubArrayWithKDistinctO3(arr: [int], k: int) -> [int]:
  n = len(arr)
  min_sum = float('inf')
  res = []
  
  for i in range(n):
    for j in range(i, n):
      curr_sum = 0
      for x in range(i, j+1):
        curr_sum += arr[x] 
      
      if curr_sum < min_sum and j-i+1 == k:
        min_sum = curr_sum
        res = [arr[i], arr[j]]
  return res 
  
def smallestSubArrayWithKDistinctO2(arr: [int], k: int) -> [int]:
  n = len(arr)
  min_sum = float('inf')
  res = [0, 0]
  
  for i in range(n):
    curr_sum = 0
    for j in range(i, n):
      curr_sum += arr[j] 
      
      if curr_sum < min_sum and j-i+1 == k:
        min_sum = curr_sum
        res = [arr[i], arr[j]]
  return res 
# arr = [1,2,2,3,1,3]
arr = [1,1]
k = 2
print(smallestSubArrayWithKDistinctO2(arr, k))


# def smallestSubArrayWithKDistinct(arr, k):
#   n = len(arr)
  
#   if n == 0 or k > n:
#     return []
  
#   left = right = 0
#   min_length = float('inf')
#   result = []
  
#   last_occurence = {}
  
#   for right in range(n):
#     last_occurence[arr[right]] = right
    
#     while len(last_occurence) > k:
      

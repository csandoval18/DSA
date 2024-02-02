# Return Kth Missing Positive Number
# arr = [2,3,4,7,11]
# k = 5

# Formula to find number of missing element at ith position
# missingNums = arr[i] - (i+1)
#               ith num   current index
# In terms of binary search the i would be the mid m
# missingNums = arr[m] - (m+1)

# BF Solution

# 1       2 3   4 5 6     7  8
# 1,2,3,4,5,6,7,8,9,10,11,12,13
# i    k
# 2 <= 5
# k+1 = 6
# 3 <= 6
# k+1 = 7
# 4 <= 7
# k+1 = 8
# 7 <= 8:
# k+1 = 9
# 11 <= 9: # false
# break
# return 9

def missingK(arr, k):
  
  for i in range(len(arr)):
    if arr[i] <= k:
      k += 1
    else:
      break
  return k
  
# Optimal Solution (Binary Search)
  
def findKthPositive(arr: [int], k: int) -> int:
  n = len(arr)
  l, r = 0, n-1
  
  while l<=r:
    m = (l+r)//2
    missing = arr[m] - (m+1)
    if missing < k:
      l = m+1
    else:
      r = m-1
  return k+r+1
  
  
# All ints in nums are unique
# This means no need to check if l == m == r in rotated arr

# No target given, therefore no need to have base case arr[m] == target 

def findMin(arr: [int]):
  n = len(arr)
  l, r = 0, n-1
  res = float('inf')
  
  while l<=r:
    m = (l+r)//2
    
    if arr[l] < arr[m]:
      res = min(res, arr[l])
      l = m + 1
    elif arr[m] < arr[r]:
      res = min(res, arr[m])
      r = m-1
  return res

nums = [3,4,1,2]


# [3,4,5,1,2]
# 3<5 | min = 3 | l=m+1
# 5<2

#      M L R
# [3,4,5,1,2]
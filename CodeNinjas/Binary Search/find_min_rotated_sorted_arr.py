# All ints in nums are unique
# This means no need to check if l == m == r in rotated arr

def findMin(arr: [int]):
  n = len(arr)
  l, r = 0, n-1
  
  while l<=r:
    m = (l+r)//2



#  L   M   R
# [3,4,5,1,2]

#  L   M   R
# [3,4,5,1,2]
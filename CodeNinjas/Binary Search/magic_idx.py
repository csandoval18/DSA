# Magic Index
# (code ninjas has a testcase error)

# t = 1

# t = 2

#  L      M   R
# [-1,-1,-1,4,4]
#   0  1  2 3 4 

#  L   M   R
# [2,3,4,5,6]
#  0 1 2 3 4

#  L   M   R
# [2,3,4,5,6]

# Input: arr = [2,3,4,5,6]
# Output: -1
# Input: arr = [-1,-1,-1,4,4,4]
# Output: 4

def magicIndex(a, n):
  l, r = 0, n-1
  
  while l<=r:
    m = (l+r)//2
    
    if a[m] == m:
      return m
    elif a[m] < m:
      l = m+1
    else:
      r = m-1
  return -1
      
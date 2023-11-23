# Every element is unique

def findKRotations(arr: [int]) -> int:
  n = len(arr)
  l, r = 0, n-1
  res = float('inf')
  i = -1
  
  while l<=r:
    m = (l+r)//2
    
    
    # If search space is already stored,
    # then arr[low] will always be
    # the min in that search space
    if arr[l] <= arr[r]:
      if arr[l] < res:
        i = l
        res = arr[l]
      break
    # If left part is sorted
    if arr[l] <= arr[m]:
      # Keep the min
      if arr[l] < res:
        i = l
        res = arr[l]
      # Eliminate left half
      l = m+1
    else: # If right part is sorted
      # Keep the minimun
      if arr[m] < res:
        i = m
        res = arr[m]
      # Eliminate right hal
      r = m-1
    return i
      
      
      
      
      
    
    
     


# To check for rotations we would rotate from the back not the front, for example:
# [1,2,3,4,5]
# If the arr is rotated 3 times then the ending arr is
# [3,4,5,1,2]
# Out: 3

# [3,4,5,1,2]
#  L   M   R

# [3,4,5,1,2]
#        L R
#        M

# [3,4,5,1,2]
#        L R
#        M

# [3,4,5,6,7,8,9,1,2]
#  L       M       R

# [3,4,5,6,7,8,9,1,2]
#            L M   R

# [3,4,5,6,7,8,9,1,2]
#            L M   R

# [3,4,5,6,7,8,9,1,2]
#                L R
#                M
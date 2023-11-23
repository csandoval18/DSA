# Every element is unique

def findKRotations(arr: [int]) -> int:
  n = len(arr)
  l, r = 0, n-1
  minVal = float('inf')
  index = -1
  
  while l<=r:
    m = (l+r)//2
    
    
    # If search space is already stored,
    # then arr[low] will always be
    # the min in that search space
    if arr[l] <= arr[r]:
      if arr[l] < minVal:
        index = l
        minVal = arr[l]
      break
    # If left part is sorted
    if arr[l] <= arr[m]:
      # Keep the min
      if arr[l] < minVal:
        index = l
        minVal = arr[l]
      # Eliminate left half
      l = m+1
    else: # If right part is sorted
      # Keep the minimun
      if arr[m] < minVal:
        index = m
        minVal = arr[m]
      # Eliminate right hal
      r = m-1
  return index
  
arr = [2,3,4,1]
print(findKRotations(arr))
      
      
      
      
      
    
    
     


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
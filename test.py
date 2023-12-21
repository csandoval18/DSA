# Trting to get opposite polarity 
# [1,1,0,0,0]
#  L   M   R
# so I need to find where the 1s end

def binarySearch(arr): 
  n = len(arr)
  l, r = 0, n-1
  
  while l<=r:
    m = (l+r)//2
    
    if arr[m] > 0:
      l = m+1
    else:
      r = m-1
  return l-1

arr = [1,1,0,0,0]
print(binarySearch(arr))
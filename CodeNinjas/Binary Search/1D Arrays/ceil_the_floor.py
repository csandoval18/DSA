# def getFloorAndCeil(a, n, x):
#   l = 0
#   r = n-1
  
#   while l<=r:
#     m = (l+r) // 2
    
#     if a[m] == x:
#       return a[m], a[m]
    
#     if a[m] >= x:
#       r = m-1
#     else:
#       l = m+1
  
#   if r < 0:
#     return -1, a[l]
#   elif l > n-1:
#     return a[r], -1
#   else:
#     return a[r], a[l]

# # a = [3,4,4,7,8,10]

# a = [6,6,7,12,16,18,19,22,23,30] 
# x = 14

# print(getFloorAndCeil(a, len(a), x))

def find_floor(a, n, x):
  l = 0
  r = n-1
  res = -1
  
  while l<=r:
    m = (l+r) // 2
    
    if a[m] <= x:
      res = a[m]
      l = m+1 # Look for smaller idx on the left
    else:
      r = m-1 # Look on the right
  return res

def find_ceil(a, n, x):
  l = 0
  r = n-1
  res = -1
  
  while l<=r:
    m = (l+r) // 2
    
    if a[m] >= x:
      res = a[m]
      r = m-1
    else:
      l = m+1
  return res
  

def find_floor_ceiling(arr, target):
  l, r = 0, len(arr)-1
  floor, ceil = None, None
  
  while l<=r:
    m = (l+r) // 2
    
    if arr[m] == target:
      return arr[m], arr[m] 
    elif arr[m] < target:
      floor = arr[m]
      l = m+1
    else:
      ceil = arr[m]
      r = m-1
  return floor, ceil 
      
 
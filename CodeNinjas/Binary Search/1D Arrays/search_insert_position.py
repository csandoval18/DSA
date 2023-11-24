def searchInsert(arr: [int], x: int) -> int:
  n = len(arr)
  l = 0
  r = n-1
  
  while l<=r:
    m = (l+r) // 2
    
    if arr[m] == x:
      return m
    elif arr[m] >= x:
      r = m-1
    else:
      l = m+1
  return l

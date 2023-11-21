def firstAndLastPosition(arr, n, k):
  def findFirst(arr, n, k):
    l, r = 0, n-1
    first = -1
    
    while l<=r:
      m = (l+r)
      
      if arr[m] == k:
        first = m
        r = m-1
      elif arr[m] > k:
        r = m-1
      else:
        l = m+1
    return first

  def findLast(arr, n, k):
    l, r = 0,  n-1
    last = -1
    
    while l<=r:
      m = (l+r)//2
      
      if arr[m] == k:
        last = m
        l = m+1
      elif arr[m] > k:
        r = m-1
      else:
        l = m+1
    return last
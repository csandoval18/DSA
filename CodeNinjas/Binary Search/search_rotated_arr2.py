def searchInARotatedSortedArrayII(arr: [], key: int) -> bool:
  n = len(arr)
  l, r = 0,  n-1
  
  while l<=r:
    m = (l+r)//2
    
    if arr[m] == key:
      return True
    elif arr[l] <= arr[m]:
      if arr[l] <= key <= arr[m]:
        r = m-1
      else:
        l = m+1
    elif arr[m] <= arr[r]: 
      if arr[m] <= key <= arr[r]:
        l = m+1
      else:
        r = m-1 
    return False
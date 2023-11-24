def floorSqrt(n):
  l, r = 1, n
  res = 0
  
  while l<=r:
    m = (l+r)//2
    
    if m*m == n:
      return m
    elif m*m < n:
      res = m
      l = m+1
    else:
      r = m-1
  return res

print(floorSqrt(22))
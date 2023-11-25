def func(m, n, x):
    tmp = 1
    
    for i in range(1, n+1):
      tmp *= m
      if tmp > x:
        return 2
    if tmp == x:
      return 1
    return 0
      
def NthRoot(n: int, x: int) -> int:
  l, r = 1,  m
  
  while l<=r:
    m = (l+r)//2
    midN = func(m, n, x)
    
    if midN == 1:
      return m
    elif midN == 0:
      l = m+1
    else:
      r = m-1
  return -1
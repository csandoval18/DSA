def myPow(x, n):
  res = 1
  nn = n
  
  if nn < 0:
    nn *= -1
    
  while nn > 0:
    if nn % 2 == 0:
      res *= x
      nn -= 1
    
    else:
      x *= x
      nn //= 2
  
  if n < 0:
    res = 1 / res
    
  return res
      
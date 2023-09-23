def myPow(x, n):
  res = 1
  nn = n
  
  # If number is negative convert it into negative number
  if nn < 0:
    nn = -1 * nn
    
  while nn > 0:
    if nn % 2 == 1:
      res = res * x
      nn = nn - 1
      
    else:
      x = x * x
      nn = nn // 2
  
  if n < 0:
    res = float(1.0/res) 
    
  return res
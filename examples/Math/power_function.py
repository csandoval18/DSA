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
      
  
def recursivePow(x: float, n:int) -> float:
  def helper(x, n):
    if x == 0: return 0
    if n == 0: return 1
    
    res = helper(x, n // 2)
    res = res*res
    
    if n % 2: 
      return x*res
    else:
      return res
  
  
  res = helper(x, abs(n))
  # Check if res is + or - 
  if n >= 0:
    return res
  else:
    return 1/res
       
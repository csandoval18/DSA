def parseBoolExpr(expression: str) -> bool:
  def f(i: int, j: int, isTrue: int):
    if i == j:
      if isTrue:
        return expression[i] == 'T'
      else:
        return expression[i] == 'F'
      
    ways = 0
    for k  in range(i+1, j, 2):
      lT = f(i, k-1, 1)
      lF = f(i, k-1, 0)
      rT = f(i+1, j, 1)
      rF = f(i+1, j, 0)
    
      # We need to find the total True and False
      if expression[k] == '&': # When pivot k is 'and'
        if isTrue:
          ways = ways + (lT * rT)
        else:
          ways = ways + (lF * rT) + (lT & rF) + (lF & rF)
      elif expression[k] == '|': # When pivot k is 'and'
        ways = ways +
        
      else:
    
      
      
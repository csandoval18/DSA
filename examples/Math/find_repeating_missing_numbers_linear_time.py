def findMissingRepeatingNumbers(a):
  n = len(a)
  
  # Find Sn and S2n
  SN = (n * (n+1)) // 2
  S2N = (n * (n+1) * (2 * n + 1)) // 6
  
  # Calculate S and S2
  S, S2 = 0, 0
  for i in range(n):
    S += a[i]
    S2 += a[i] * a[i]
  
  # S-Sn = X-Y:
  val1 = S - SN
  
  # S2-S2n = X^2-Y^2
  val2 = S2 - S2N
  
  # Find X+Y = (X^2-Y^2)/(X-Y)
  val2 = val2 // val1
  
  # Find X and Y: X = ((X+Y)+(X-Y))/2 and Y = X-(X-Y),
  # Here, X-Y = val1 and X+Y = val2
  x = (val1 + val2) // 2
  y = x - val1
  
  return [x, y]
  
def findMissingRepeatingNubmers(a: [int]) -> [int]:
  n = len(a)
  xr = 0
  
  # Step 1: Find XOR of all elements:
  for i in range(n):
    xr = xr ^ a[i]
    xr = xr ^ (i + 1)
    
  # Step 2: Find the differentiating bit number:
  number = (xr & ~(xr-1))
  
  # Step 3: Group the numbers
  
  
    
    
  
  
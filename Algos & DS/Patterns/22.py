# n=3
# 33333
# 32223
# 32123
# 33333

# n=4
# 4444444
# 4333334
# 4322234
# 4321234
# 4322234
# 4333334
# 4444444

def getNumberPattern(n: int) -> None:
  for i in range(2*n-1):
    for j in range(2*n-1):
      top = i
      bottom = j
      right = (2*n-2)-j
      left = (2*n-2)-i
      
      print(n-min(min(top, bottom), min(left, right)), end=" ")
    print() 

getNumberPattern(3)
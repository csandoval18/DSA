# 1 
# 0 1 
# 1 0 1 

# 0 = even 0%2=0
# 1 = uneven 1%2=1

def nBinaryTriangle(n: int) -> None:
  x = 1
  for i in range(n):
    if i%2 == 0:
      x = 1
    else:
      x = 0
    
    for j in range(i+1):
      print(x, end=" ")
      x = 1-x
      
    print()

nBinaryTriangle(3)
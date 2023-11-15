def nStarTriangle(n: int) -> None:
  for i in range(n):
    for j in range(i+1):
      print("*", end="")
    print()
    
  for i in range(n-1,-1,-1):
    for j in range(i):
      print("*", end="")
    print()
  
nStarTriangle(3)
# * * * * * * 
# * *     * * 
# *         * 
# *         * 
# * *     * * 
# * * * * * * 

def symmetry(n: int) -> None:
  for i in range(n):
    for j in range(n-i):
      print("*", end=" ")
    for j in range(1, 2*i+1):
      print(" ", end=" ")
    for j in range(n-i):
      print("*", end=" ")
    print()
    
  for i in range(n):
    for j in range(i+1):
      print("*", end=" ")
    for j in range(1, 2*n - (2*i+1)):
      print(" ", end=" ")
    for j in range(i+1): 
      print("*", end=" ")
    print()
  
symmetry(3)
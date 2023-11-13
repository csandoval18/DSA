# Pattern 8

# *****
#  ***
#   *

def nStarTriangle(n: int) -> None:
  for i in range(n):
    for j in range(i):
      print(" ", end="")
    for j in range(2*n-(2*i+1)):
      print("*", end="")
    # for j in range(i):
    #   print(" ", end="")
    print()

      
nStarTriangle(3)
  
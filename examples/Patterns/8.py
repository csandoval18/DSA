<<<<<<< HEAD
# Pattern 7

#   *
#  ***
# *****

def nNumberTriangle(n: int) -> None:
  for i in range(n-i-1):
    for j in range(i):
      print(" ", end="")
    for j in range(2*i+1):
      print("*", end="")
    for j in range(n-i-1):
      print(" ", end="")
      
nNumberTriangle(3)
=======
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
>>>>>>> 3d75a4588b11131016e4d3ccdf523c54a9bf6615
  
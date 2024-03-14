# n = 3

# ***
# * *
# ***

# n=5

# *****
# *   *
# *   *
# *   *
# *****

def getStarPattern(n: int) -> None:
  for i in range(n):
    for j in range(n):
      if i==0 or i==n-1 or j==0 or j==n-1:
        print("*", end="")
      else:
        print(" ", end="")
    print()
    
getStarPattern(3) 

    
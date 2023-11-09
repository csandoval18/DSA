# Pattern 5

# ***
# ** 
# *

def seeding(n: int) -> None:
  for i in range(n, -1, -1):
    for j in range(i):
      print("*", end=" ")
    print()

seeding(3)
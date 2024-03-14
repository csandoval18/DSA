# Pattern 3

# 1
# 12
# 123

def nTriangle(n: int) -> None:
  for i in range(n+1):
    for j in range(i):
      print(j+1, end=" ")
    print()
      
nTriangle(3)
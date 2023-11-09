# Pattern 6

# 123
# 12
# 1

def nNumberTriangle(n: int) -> None:
  for i in range(n, -1, -1):
    for j in range(i):
      print(j+1, end=" ")
    print()

nNumberTriangle(3)
  
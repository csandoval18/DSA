# Pattern 4

# 1
# 22
# 333

def triangle(n:int) -> None:
  x = 1
  for i in range(n):
    for j in range(i+1):
      print(x, end=" ")
    x += 1
    print()

triangle(3)
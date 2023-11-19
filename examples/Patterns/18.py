# n=3
# C
# C B 
# C B A

# n=2
# B
# B A

# n=1
# C

# def alphaTriangle(n: int) -> None:
#   for i in range(n):
#     for j in range(i+1):
#       print(chr(ord('A') - i + j), end=" ")
#     print()
  
# alphaTriangle(3)

def alphaTriangle(n: int) -> None:
  char = 'A'
  
  for i in range(n):
    for j in range(i+1):
      print(chr(ord(char)+n-1-j), end=" ")
    print()

alphaTriangle(2)
#     A
#   A B A
# A B C B A

# def alphaHill(n: int) -> None:
#   char = 'A'
  
#   for i in range(n):
#     for j in range(n-i-1):
#       print(" ", end="")
#     for j in range(2*i+1):
#       print(chr(ord(char) + j), end=" ")
#     print()
  
# alphaHill(3)

def alphaHill(n: int) -> None:
  for i in range(n):
    for j in range(n-i-1):
      print(" ", end="")
    
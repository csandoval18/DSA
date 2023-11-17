# A
# A B
# A B C

def nLetterTriangle(n: int) -> None:
  char = 'A'
  
  for i in range(n):
    for j in range(i+1):
      print(chr(ord(char)+j), end=" ")
    print()

nLetterTriangle(3)
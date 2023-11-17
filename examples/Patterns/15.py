# A B C
# A B
# A

def nLetterTriangle(n: int) -> None:
  char = 'A'
  
  for i in range(n):
    for j in range(n, i, -1):
      print(chr(ord(char)+j), end="")
    print() 

nLetterTriangle(3)
# A
# B B
# C C C

def alphaRamp(n: int) -> None:
  char = "A"
  
  for i in range(n):
    for j in range(i+1):
      print(char, end=" ")
    print()
    char = chr(ord(char) + 1) 
  
alphaRamp(3)
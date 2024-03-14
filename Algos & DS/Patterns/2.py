# Pattern 2

#  *
#  **
#  ***

def triangle(n):
  for i in range(n):
    for j in range(i+1):
       print("*", end=" ")
    print()
    
triangle(3)
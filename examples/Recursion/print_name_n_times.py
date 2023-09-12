def printName(i, n):
  # Base case
  if i > n:
    return
    
  print("Christian")
  printName(i+1, n)

printName(1, 3)

# Recursion Tree

# f(1,3)
#    | print("Christian")
# f(2,3)
#    | print("Christian")
# f(3,3)
#    | print("Christian")
# f(4,3) 
# Stops loop due to base case i > n | 4 > 3
    
  
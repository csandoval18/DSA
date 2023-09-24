# With loops printed
def printNosSteps(x: int) -> [int]:
  arr = []
  
  def printNosHelper(x, arr):
    if x == 0:
      return 
      
    print("x:", x)
    print("arr1:", arr)
    arr = [x] + arr
    print("arr2:", arr)
    print("\n")
    return printNosHelper(x-1, arr)
  
  return printNosHelper(x, arr)
  
  
  
def printNos(x: int) -> [int]:
  res = []
  def printNosHelper(x, arr):
    if x == 0:
      return res
      
    printNosHelper(x-1, res)
    res.append(x)
    return res
  
  return printNosHelper(x, res)
    
x = 5
print(printNos(x))
from typing import List

# BF
def sequentialDigits(low: int, high: int) -> List[int]:
  def isSequential(num: int) -> bool:
    last = num%10
    num = num//10
    
    while num > 0:
      if num%10 != last-1:
        return False
      last = num % 10
      num = num // 10
      
    return True
    
  res = []
  while low < high:
    if isSequential(low):
      res.append(low)
    low += 1
    
  return res
  
num = 123
print(sequentialDigits(100,300))
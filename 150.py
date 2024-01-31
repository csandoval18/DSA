from typing import List

def evalRPN(token: List[str]) -> int:
  n = len(token)
  
  for i in range(n):
    for j in range(i, n):
      
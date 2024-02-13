from typing import List

def letterCombinations(digits: str) -> List[str]:
  mappings = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
  
  n = len(digits)
  if n == 0:
    return ''
  res = []

  def backtrack(path, startindex):
    if len(path) == n:
      res.append(''.join(path))
      return 
    
    for c in mappings[digits[startindex]]:
      path.append(c)
      backtrack(path, startindex+1)
      path.pop()

  backtrack([], 0)
  return res

            
  
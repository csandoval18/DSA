from typing import List

def letterCombinations(digits: str) -> List[str]:
  mappings = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
  
  n = len(digits)
  if n == 0:
    return ''
    
  res = []
  def bt(i: int, path: List[str]):
    if len(path) == n:
      res.append(''.join(path))
      return 
    
    for c in mappings[digits[i]]:
      path.append(c)
      bt(i+1, path)
      path.pop()

  bt(0, [])
  return res

digits = "23"
print(letterCombinations(digits))

            
def letterCombinations2(digits: str) -> List[str]: 
  mappings = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
  n = len(digits)
  res = []
  
  def f(i: int, ds: str) -> None:
    if i == n:
      res.append(ds)
      return
    
    for char in mappings[digits[i]]:
      f(i+1, ds+char)

  if digits:
    f(0, "")
  return res
  
digits = "23"
print(letterCombinations2(digits))
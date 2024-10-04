from typing import List

# op = open parenthesis count
# m = str curr len
def generateParenthesis(n: int) -> List[str]:
  def backtrack(m: int, op: int, st: str) -> None:
    if m == n*2:
      res.append(st)
      return
    
    if op < n:
      backtrack(m+1, op + 1, st + '(')
      
    if m - op < op:
      backtrack(m + 1, op, st + ')')
  
  res = []
  backtrack(0, 0, "")
  return res


# Chatgpt
def generateParenthesisGPT(n):
  def backtrack(op, cp, s):
    if len(s) == n*2:
      res.append(s)
      return
    
    # Dont need to remove last char from s since string are immutable
    # so a copy is passed to the other recusive calls
    if op < n:
      backtrack(op+1, cp, s + '(')
      
    if cp < op:
      backtrack(op, cp+1, s + ')')

  res = []
  backtrack(0, 0, '')
  return res
  
n = 3
print(generateParenthesis(n))
print(generateParenthesisGPT(n))
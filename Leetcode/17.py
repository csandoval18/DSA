from typing import List

def letterCombinations(digits: str) -> List[str]:
  n = len(digits)
  dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
  ds = []
  res = []
  
  def backtrack(idx: int):
    if len(ds) == n:
      res.append(ds[:])
      return
    
    for char in dic[digits[idx]]:
      backtrack(ds + char)
        
  if digits:
    backtrack(ds)
  return res
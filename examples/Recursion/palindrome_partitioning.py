from typing import List

def partition(s: str) -> List[List[str]]:
  n = len(s)
  res = []
  
  def isPalindrome(s: str, l: int, r: int):
    while l<r:
      if s[l] != s[r]:
        return False
      l += 1
      r -= 1
    return True
  
  def backtrack(idx: int, path: List[int]):
    if idx == n:
      res.append(path[:])
      return
      
    for i in range(idx, n):
      if isPalindrome(s, idx, i):
        path.append(s[idx:i+1])
        
  backtrack(0, [])
  return res

s = "aab"
print(partition(s))



def palindrome(string: str) -> bool:
  n = len(string)
  l, r = 0, n-1
  
  while l<r:
    if string[l] != string[r]:
      return False
    l += 1
    r -= 1
  return True
    
string = "aba"
print(palindrome(string))
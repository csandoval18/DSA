from typing import List

def partition(s: str) -> List[List[str]]:
  n = len(s)
  res = []

  def isPalindrome(s: str) -> bool:
    return s == s[::-1]

  def backtrack(idx: int, path: List[str]):
    if idx == n:
      res.append(path[:])
      return

    for i in range(idx, n):
      substring = s[idx:i + 1]
      if isPalindrome(substring):
        path.append(substring)
        backtrack(i + 1, path)
        path.pop()

  backtrack(0, [])
  return res
s = "aab"
print(partition(s))


def partition(s: str) -> List[List[str]]:
  n = len(s)
  res = []
  
  def inPalindrome(s: str) -> bool:
    return s == s[::-1]
  
  def backtrack(idx: int, ds: List[str]) -> None:
    if idx == n:
      res.append(ds[:])
      return
    
    

# def palindrome(string: str) -> bool:
#   n = len(string)
#   l, r = 0, n-1
  
#   while l<r:
#     if string[l] != string[r]:
#       return False
#     l += 1
#     r -= 1
#   return True
    
# string = "aba"
# print(palindrome(string))
from typing import List

# 131. Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

def partition(s: str) -> List[List[str]]:
  n = len(s)
  res = []
  
  def isPalindrome(s: str) -> bool:
    return s == s[::-1]
    
  def bt(idx: int, path: List[str]):
    if idx == n:
      res.append(path[:])
      return
    
    for i in range(idx, n):
      ss = s[idx: i+1]
      if isPalindrome(ss):
        path.append(ss)
        bt(i+1, path)
        path.pop()
  
  bt(0, [])
  return res
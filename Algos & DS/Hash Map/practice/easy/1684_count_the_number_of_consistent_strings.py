from typing import List


class Solution:
  def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    allowed_chars = set(allowed)
    consistent_strings = 0

    for word in words:
      for i, c in enumerate(word):
        if c not in allowed_chars:
          break
        if i == len(word)-1:
          consistent_strings += 1
      
    return consistent_strings

class Solution:
  def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    allowed_chars = set(allowed)
    misses = 0
    
    for i in words:
      for j in i:
        if j not in allowed_chars:
          misses +=1
          break
    return len(words)-misses
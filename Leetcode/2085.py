from collections import Counter
from typing import List

def countWords(words1: List[str], words2: List[str]) -> int:
  w1_cnt = Counter(words1)
  w2_cnt = Counter(words2)
  seen = set()
  res = 0
  
  for word in w1_cnt:
    if word in seen:
      continue
    elif w1_cnt[word] == 1 and w2_cnt[word] == 1:
      res += 1
      seen.add(word)
    
  for word in w2_cnt:
    if word in seen:
      continue
    elif w1_cnt[word] == 1 and w2_cnt[word] == 1:
      res += 1
      seen.add(word)
  
  return res

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
print(countWords(words1, words2))

def countWords(words1: List[str], words2: List[str]) -> int:
  w1 = Counter(words1)
  w2 = Counter(words2)
  res = 0
  for w in words1:
    if w1[w] == 1 and w2[w] == 1:
      res += 1
  
  return res
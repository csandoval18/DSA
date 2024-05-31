from collections import defaultdict, deque
from typing import List

def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
  wordList = set(wordList) # Convert wordlist to set for faster access
  if endWord not in wordList:
    return []
  
  # Dictionary to hold all possible transformations
  hm = defaultdict(list)
  length = len(beginWord)
  
  for word in wordList:
    for i in range(length):
      hm[word[:i] + "*" + word[i+1:]].append(word)
  
  queue = deque([(beginWord, [beginWord])])
  visited = set([beginWord])
  found = False
  paths = []
  
  while queue and not found:
    
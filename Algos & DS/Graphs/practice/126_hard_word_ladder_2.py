from collections import defaultdict, deque
from typing import List

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
  wordList = set(wordList) # Convert wordlist to set for faster access
  if endWord not in wordList:
    return []
  
  # Dictionary to hold all possible transformations
  hm = defaultdict(list)
  length = len(beginWord)
  
  for word in wordList:
    for i in range(length):
      hm[word[:i] + "*" + word[i+1:]].append(word)
  
  # BFS
  queue = deque([(beginWord, [beginWord])])
  visited = set([beginWord])
  found = False
  paths = []
  
  while queue and not found:
    local_visited = set()
    for _ in range(len(queue)):
      curr_word, path = queue.popleft()
      
      for i in range(length):
        inter_word = curr_word[:i] + '*' + curr_word[i+1:]
        
        for word in hm[inter_word] :
          if word == endWord:
            found = True
            paths.append(path + [word])
          if word not in visited:
            local_visited.add(word)
            queue.append((word, path + [word]))
    visited.update(local_visited)
    
  return paths

def findLadders2(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
  wordSet = set(wordList)
  if endWord not in wordSet:
    return []
  
  queue = deque([beginWord])
  visited = {}
  hm = {}
  layers[beginWord] = 
from collections import defaultdict, deque
from typing import List

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
  if endWord not in wordList:
    return 0 
  
  L = len(beginWord)
  
  # Create a dict of all possible intermediate words
  all_combo_dict = defaultdict(list)
  
  for word in wordList:
    for i in range(L):
      inter_word = word[:i] + '*' + word[i+1:]
      all_combo_dict[inter_word].append(word)
      
  queue = deque([(beginWord, 1)]) # Declare BFS queue
  # Visisted dic to prevent cycles
  visited = {beginWord: True}
  
  while queue:
    curr_word, level = queue.popleft()
    for i in range(L):
      inter_word = curr_word[:i] + '*' + curr_word[i+1:]
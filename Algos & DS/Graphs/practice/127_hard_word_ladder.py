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
      for word in all_combo_dict[inter_word]:
        if word == endWord:
          return level + 1
        if word not in visited:
          visited[word] = True
          queue.append((word, level+1))
    all_combo_dict[inter_word] = []
    
  return 0
          

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
  # Convert the word list to a set for O(1) look-ups
  wordSet = set(wordList)
  
  # If the endWord is not in the wordList, no valid transofrmation is possible
  if endWord not in wordSet:
    return 0
  
  queue = deque([(beginWord, 1)])
  while queue:
    currWord, length = queue.popleft()
    
    # If current word is the end word, we've found the shortest transformation
    if currWord == endWord:
      return length
    
    # Try changing each char in the curr word
    for i in range(len(currWord)):
      for c in "abcdefghijklmnopqrstuvwxyz"
      # Create a new word by changing the i-th character to c
      newWord = currWord[:i] + c + currWord[i+1:]
      
      # If the new word is in the wordSet, add it to the queue and remove from the set
      if newWord in wordSet:
        queue.append((newWord, length+1))
        wordSet.remove(newWord)

  # If we exhaust the queue without finding the endWord, no transformation sequence exists
  return 0
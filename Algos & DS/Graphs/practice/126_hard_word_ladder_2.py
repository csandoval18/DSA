from collections import defaultdict, deque
from typing import List

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
  # Convert the wordList into a set for O(1) lookups
  word_set = set(wordList)
  # Initialize the queue with the beginWord in a list
  q = deque([[beginWord]])
  # List to keep track of the words used at the current BFS level
  used_on_level = [beginWord]
  level = 0
  # List to store the final transformation sequences
  ans = []
  
  while q:
    # Get the current sequence from the queue
    seq = q.popleft()
    
    # If we are at a new level, remove all the words used in the previous level
    if len(seq) > level:
      level += 1
      for word in used_on_level:
        if word in word_set:
          word_set.remove(word)
      used_on_level = []
  
    # Get the last word in the current sequence
    word = seq[-1]
    
    # If the last word is the endWord, check the conditions to add it to the answer list
    if word == endWord:
      if not ans or len(ans[0]) == len(seq):
        ans.append(seq)
      continue
    
    # Try changing each character of the word to find all possible transformations
    for i in range(len(word)):
      original_char = word[i]
      for c in 'abcdefghijklmnopqrstuvwxyz':
        word = word[:i] + c + word[i+1:]
        if word in word_set:
          # Create a new sequence with the transformed word and add it to the queue
          new_seq = copy.deepcopy(seq)
          new_seq.append(word)
          q.append(new_seq)
          # Mark this word as used on the current level
          used_on_level.append(word)
      # Restore the original word
      word = word[:i] + original_char + word[i+1:]
      
  return ans
  
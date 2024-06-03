from collections import defaultdict, deque
import copy
from typing import List

def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    if endWord not in wordList:
      return []

    # Initialize data structures
    wordList = set(wordList)  # Convert to set for O(1) look-ups
    parents = defaultdict(list)
    levels = {beginWord: 0}
    queue = deque([beginWord])
    found = False
    word_len = len(beginWord)
    
    # BFS to find shortest path
    while queue and not found:
      current_level_size = len(queue)
      for _ in range(current_level_size):
        word = queue.popleft()
        current_level = levels[word]
        for i in range(word_len):
          for c in 'abcdefghijklmnopqrstuvwxyz':
            next_word = word[:i] + c + word[i+1:]
            if next_word in wordList:
              if next_word not in levels:
                levels[next_word] = current_level + 1
                queue.append(next_word)
              if levels[next_word] == current_level + 1:
                parents[next_word].append(word)
              if next_word == endWord:
                found = True
      wordList -= set(levels.keys())  # Remove words of the current level to prevent loops

    # If the endWord was not found, return an empty list
    if endWord not in levels:
        return []
    
    # DFS to build all paths
    def dfs(word):
        if word == beginWord:
            return [[beginWord]]
        return [[word] + path for parent in parents[word] for path in dfs(parent)]

    # Generate all paths from endWord to beginWord
    return [path[::-1] for path in dfs(endWord)]

# Faster by a bit but seems more complicated
class Solution:
  def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    d = defaultdict(list)
    
    for word in wordList:
      for i in range(len(word)):
        d[word[:i] + "*" + word[i + 1:]].append(word)

    if endWord not in wordList:
      return []

    visited1 = defaultdict(list)
    q1 = deque([beginWord])
    visited1[beginWord] = []

    visited2 = defaultdict(list)
    q2 = deque([endWord])
    visited2[endWord] = []

    ans = []

    def dfs(v, visited, path, paths):
      path.append(v)
      if not visited[v]:
        if visited is visited1:
          paths.append(path[::-1])
        else:
          paths.append(path[:])
      for u in visited[v]:
        dfs(u, visited, path, paths)
      path.pop()

    def bfs(q, visited1, visited2, frombegin):
      level_visited = defaultdict(list)
      for _ in range(len(q)):
        u = q.popleft()

        for i in range(len(u)):
          for v in d[u[:i] + "*" + u[i + 1:]]:
            if v in visited2:
              paths1 = []
              paths2 = []
              dfs(u, visited1, [], paths1)
              dfs(v, visited2, [], paths2)
              if not frombegin:
                paths1, paths2 = paths2, paths1
              for a in paths1:
                for b in paths2:
                  ans.append(a + b)
            elif v not in visited1:
              if v not in level_visited:
                q.append(v)
              level_visited[v].append(u)
      visited1.update(level_visited)

    while q1 and q2 and not ans:
        if len(q1) <= len(q2):
            bfs(q1, visited1, visited2, True)
        else:
            bfs(q2, visited2, visited1, False)

    return ans
            
          

# Sol 1 with comments explaining:
def findLadders(beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
  # Convert word list to a set for faster lookups.
  wordList = set(wordList)
  
  # If the endWord is not in the word list, there is no valid transformation
  if endWord not in wordList:
    return []
  
  parents = defaultdict(list) # Dictionary to store the parents words of each word.
  levels = { beginWord: 0 } # Dictionary to store the level (distance from beginWord) of each word.
  queue = deque([beginWord]) # Queue for BFS, starting with the beginWord.
  found = False # Flag to indicate if we have found the endWord.
  word_len = len(beginWord) # Length of each word.
  
  # Perform BFS to find the shortest paths.
  while queue and not found:
    curr_level_len = len(queue)
    
    for _ in range(curr_level_len):
      word = queue.popleft()
      curr_level = levels[word]
      
      for i in range(word_len):
        # Try changing each letter in the word to every letter from 'a' to 'z'.
        for c in 'abcdefghijklmopqrstuvwxyz':
          next_word = word[:i] + c + word[i+1:]
          
          # If the new word is in the word list.
          if next_word in wordList:
            # If the new word is not yet visited, mark its level and add it to the queue.
            if next_word not in levels:
              levels[next_word] = curr_level + 1
              queue.append(next_word)
            # If the new word is at the next level, record the parent word.
            if levels[next_word] == curr_level + 1:
              parents[next_word].append(word)
            # If we have reached the endWord, set the found flag to True.
            if next_word == endWord:
              found = True
      # Remove all words that have been processed to avoid loops
      wordList -= set(levels.keys())
      
  # If the endWord was not found, return an empty list.
  if endWord not in levels:
    return []
  # BFS to build all paths from endWord to beginWord.
  def dfs(word: str):
    # If we reach the beginWord, return a list with the beginWord.
    if word == beginWord:
      return [[beginWord]]
    # Otherwise, build paths by adding the current word to the paths from its parents.
    return [[word] + path for parent in parents[word] for path in dfs(parent)]
  
  # Generate all paths from endWord to beginWord and reverse each path.
  return [path[::-1] for path in dfs(endWord)]
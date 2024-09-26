from typing import List

class TrieNode:
  def __init__(self):
    self.children = {}
    self.count = 0 # Keeps track of how many times a prefix appears

class Trie:
  def __init__(self) -> None:
    self.root = TrieNode()
  
  def insert(self, word):
    node = self.root
    for char in word:
      if char not in node.children:
        node.children[char] = TrieNode()
        
      node = node.children[char]
      node.count += 1 # Increment the count for this prefix
  
  def get_prefix_score(self, word):
    node = self.root
    score = 0
    
    for char in word:
      node = node.children[char]
      score += node.count # Add the count for the current prefix
    return score

class Solution:
  def sumPrefixScores(self, words: List[str]) -> List[int]:
    trie = Trie()
    
    # Insert all words into the trie
    for word in words:
      trie.insert(word)
      
    # Compute the sum of prefix scores for each word
    res = []
    for word in words:
      res.append(trie.get_prefix_score(word))
    return res
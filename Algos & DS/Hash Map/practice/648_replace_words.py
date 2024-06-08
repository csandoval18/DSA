from typing import Counter, List

class Solution:
  def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    root_set = set(dictionary) # Create a set of dictionary roots for O(1) lookups
    print(root_set)
    
    def replace(word: str):
      # Find the shortest root that is a prefix
      for i in range(1, len(word) + 1):
        if word[:i] in root_set:
          return word[:i]
      return word
      
    # Split the sentence into words array
    words = sentence.split()
    print("split words:", words)
    # Replace each word with the shortest root
    replaced_words = [replace(word) for word in words]
    
    # Join the words back into a sentence string
    return " ".join(replaced_words)

class Solution1:
  def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    root_set = set(dictionary)
    
    def replace(split_words: str) -> str:
      for i in range(1, len(word)+1):
        if word[:i] in root_set:
          return word[:i]
      return word
    
    split_words = sentence.split()
    replaced_words = []
    
    for word in split_words:
      replaced_words.append(replace(word))
    
    return " ".join(replaced_words)


# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# Trie solution Optimal

class TrieNode:
  def __init__(self) -> None:
    self.children = {}
    self.wordEnd = False

class Trie:
  def __init__(self) -> None:
    self.root = TrieNode()
  
  def insert(self, word: str):
    node = self.root
    
    for c in word:
      if c not in node.children:
        node.children[c] = TrieNode()
      node = node.children[c]
    node.wordEnd = True
  
  def search_shortest_prefix(self, word: str):
    node = self.root
    prefix = ""
    
    for c in word:
      if c not in node.children:
        break
      
      node = node.children[c]
      prefix += c
      
      if node.wordEnd:
        return prefix
        
    return word
  
def replaceWords(dictionary: List[str], sentence: str):
  trie = Trie()
  # Insert all roots into the trie
  for root in dictionary:
    trie.insert(root)
  
  # Split the sentence into words
  words = sentence.split()
  # Replace each word with the shortest root
  res = []
  for word in words:
    res.append(trie.search_shortest_prefix(word))
  
  # Join the words abck into a setence string
  return " ".join(res)
    
      
# s = Solution()
dictionary = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# print(s.replaceWords(dictionary, sentence))
print(replaceWords(dictionary, sentence))

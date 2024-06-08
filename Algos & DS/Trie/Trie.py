class TrieNode:
  def __init__(self) -> None:
    self.childNode = [None] * 26
    self.wordEnd = False
    
class Trie:
  def __init__(self) -> None:
    self.root = TrieNode()
    
  # Function to insert a key into the trie
  def insert(self, key: str):
    currNode = self.root
    
    for c in key:
      idx = ord(c) - ord('a')
      if not currNode.childNode[idx]:
        currNode.childNode[idx] = TrieNode()
      currNode = currNode.childNode[idx]
    currNode.wordEnd = True
  
  def search(self, key: str):
    currNode = self.root
    
    for c in key:
      idx = ord(c) - ord('a')
      if not                  
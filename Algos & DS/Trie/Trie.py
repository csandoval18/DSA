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
      if not currNode.childNode[idx]:
        return False
        
      currNode = currNode.childNode[idx]
    return currNode.wordEnd
      
if __name__ == "__main__":
  trie = Trie()
  inputStrings = ["and", "ant", "do", "geek", "dad", "ball"]

  # Insert each string into the Trie
  for word in inputStrings:
      trie.insert(word)

  searchQueryStrings = ["do", "geek", "bat"]
  # Search for each string and print whether it is found in the Trie
  for query in searchQueryStrings:
      print("Query String:", query)
      if trie.search(query):
          print("The query string is present in the Trie")
      else:
          print("The query string is not present in the Trie")

class TrieNode1:
  def __init__(self) -> None:
    self.children = {}
    self.wordEnd = False

class Trie1:
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
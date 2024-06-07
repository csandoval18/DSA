from typing import Counter, List


# class Solution:
    # def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    #   # Make dictionary array into dictionary map
    #   dict_maps = []
    #   for root in dictionary:
    #     tmp = Counter(root)
    #     dict_maps.append(tmp)
      
    #   for c in sentence:
    #     for hm in dict_maps:
    #       if c in hm:
    #         hm[c] -= 1
            
            
class Solution:
  def replaceWords(self, dictionary: List[str], sentence: str) -> str:
    root_set = set(dictionary) # Create a set of dictionary roots for O(1) lookups
    
    def replace(word: str):
      # Find the shortest root that is a prefix
      for i in range(1, len(word) + 1):
        if word[:i] in root_set:
          return word[:i]
      return word
      
    # Split the sentence into words array
    words = sentence.split()
    # Replace each word with the shortest root
    replaced_words = [replace(word) for word in words]
    
    # Join the words back into a sentence string
    return " ".join(replaced_words)
      
#       # Traverse through sentence characters and lookup char in three dcitionary maps
      
dictionary = ["cat","bat","rat"]
if "cat" in dictionary:
# sentence = "the cattle was rattled by the battery"
# for word in sentence:
#   print(word)
# Output: "the cat was rat by the bat"
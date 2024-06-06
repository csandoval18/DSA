from collections import defaultdict
from typing import Counter, List

class Solution:
  def commonChars(self, words: List[str]) -> List[str]:
    res = []
    word_counters = []
    n = len(words)

    for i in range(1, n):
      tmp = Counter(words[i])
      word_counters.append(tmp)

    for c in words[0]:
      for counter in word_counters:
        char_in_all_words = True
        if c not in counter :
          char_in_all_words = False
          break
          
        counter[c] -= 1
        if counter[c] <= 0:
          del counter[c]
      
      if char_in_all_words:
        res.append(c)
        
    return res

class Solution2:
  def commonChars(self, words: List[str]) -> List[str]:
    common_chars = list(words[0])
    for word in words[1:]:
      new_common_chars = []
      for char in common_chars:
        if char in word:
          new_common_chars.append(char)
          # word = word.replace(char,'',1)
          word = word.replace(char, '', 1)
      common_chars = new_common_chars
    return common_chars

s = Solution()
words = ["bella","label","roller"]
# Output: ["e","l","l"]
print(s.commonChars(words))

words = ["cool","lock","cook"]
print(s.commonChars(words))


# Replace method for string in python

original_string = "Hello, world!"
modified_string = original_string.replace("world", "there")
print(modified_string)  # Output: "Hello, there!"

original_string = "apple, apple, apple"
modified_string = original_string.replace("apple", "orange", 2)
print(modified_string)  # Output: "orange, orange, apple"
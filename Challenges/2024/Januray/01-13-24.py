from collections import Counter

# 1657. Determine if Two Strings Are Close

# Two strings are considered close if you can attain one from the other using the following operations:

# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb

# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either string as many times as necessary.

# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

def closeStrings(word1: str, word2: str) -> bool:
  w1 = Counter(word1)
  w2 = Counter(word2)
  a = Counter(w1.values())
  b = Counter(w2.values())
  c = a-b
  
  return w1.keys() == w2.keys() and len(c) == 0 
  
# Explanation based on hints: 
# Hint 1: Operation 1 allows you to freely reorder the string.
# Hint 2: Operation 2 allows you to freely reassign the letters' frequencies.

# So we should really worry about the counts/values of the keys/chars in each word since they can be reassgined to another value
# If the values are the same then the len of c should be equal to 0
# comparing the keys in the return statement is done to make sure the chars are present in both words
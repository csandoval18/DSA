from heapq import heapify, heappop, heappush
from typing import Counter

# You are given a string word containing lowercase English letters.

# Telephone keypads have keys mapped with distinct collections of lowercase English letters,
# which can be used to form words by pushing them. For example, the key 2 is mapped with
# ["a","b","c"], we need to push the key one time to type "a", two times to type "b", and
# three times to type "c".

# It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters. The keys
# can be remapped to any amount of letters, but each letter must be mapped to exactly one
# key. You need to find the minimum number of times the keys will be pushed to type the string word.

# Return the minimum number of pushes needed to type word after remapping the keys.
# An example mapping of letters to keys on a telephone keypad is given below. Note that 1,
# *, #, and 0 do not map to any letters.


# Basically we need to spread out the chars of word into the start of each key (2,3,4,5,6,7,8,9)
# This way we minimize the amount of clicks needed to type out the word in the num pad.

# Hash Map solution:
class Solution:
  def minimumPushes(self, word: str) -> int:
    hm = Counter(word) # Frequency map to store countof each letter
    pq = [-val for val in hm.values()]
    heapify(pq)
    
    res = 0
    i = 0
    
    while pq:
      res += (1 + (i // 8)) * (-heappop(pq))
      i += 1
      
    return res

# Sorting solution (Optimal SO):
class Solution:
  def minimumPushes(self, word: str) -> int:
    l=[0]*(32)
    
    for i in range(26):
      l[i]=word.count(chr(97+i))
      
    l.sort(reverse=True)
    
    res=0
    for i in range(4):
      for j in range(8):
        res+=(i+1)*l[8*i+j]
        
    return res
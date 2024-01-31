from collections import Counter
from typing import List

def uniqueOccurences(arr: List[int]) -> bool:
  hm = Counter(arr)
  seen = set()
  
  for num in hm.values():
    if num in seen:
      return False
    seen.add(num)
  return True

arr = [1,2,2,1,1,3]
print(uniqueOccurences(arr))
  
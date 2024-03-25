from collections import Counter
from typing import List

def maxFrequencyElements(self, nums: List[int]) -> int:
  res = 0
  freq = Counter(nums)

  maxFreq = max(freq.values())
  for f in freq.values():
    if f == maxFreq:
      res += maxFreq
  return res

def maxFrequencyElements(nums: List[int]) -> int:
  freq = Counter(nums)
  max_count = max(freq.values())
  res = 0
  
  for count in freq.values():
    if count == max_count:
      res += count
  
  return res
from typing import Counter, List


class Solution:
  def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    hm = Counter(arr1)
    res = []
    
    for num in arr2:
      while hm[num] > 0:
        res.append(num)
        [num] -= 1
        
        if hm[num] == 0:
          del hm[num]
    for num in sorted(hm.keys()):
      while hm[num] > 0:
        res.append(num)
        hm[num] -= 1
        
    return res
from typing import List


class Solution:
  def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
    hm = {}
    
    for name, height in zip(names, heights):
      hm[height] = name
      
    sorted_dict = sorted(hm.items(), reverse=True)
    res = []
    for height, name in sorted_dict:
      res.append(name)
    return res

names = ["Mary","John","Emma"]
heights = [180,165,170]
s = Solution()
print(s.sortPeople(names, heights))
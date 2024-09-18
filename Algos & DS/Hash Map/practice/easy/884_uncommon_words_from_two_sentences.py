from typing import Counter, List


class Solution:
  def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    res = []
    s1_lst = s1.split(" ")
    s2_lst = s2.split(" ")
    s1_hm = Counter(s1_lst)
    s2_hm = Counter(s2_lst)
    
    for word in s1_lst:
      if word in res:
        continue
      elif s1_hm[word] == 1 and word not in s2_hm: 
        res.append(word)
    
    for word in s2_lst:
      if word in res:
        continue
      elif s2_hm[word] == 1 and word not in s1_hm:
        res.append(word)
    
    return res

class SolutionSimplified:
  def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
    l1 = s1.split()
    l2 = s2.split()
    l = l1+l2
    
    res = []
    for i in l:
      if l.count(i) == 1:
        res.append(i)
    return res      

s1 = "this apple is sweet"
s2 = "this apple is sour"
# Output: ["sweet","sour"]

s = Solution()
print(s.uncommonFromSentences(s1, s2))
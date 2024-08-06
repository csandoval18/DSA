from typing import Counter, List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
      cnt = Counter(arr)
      
      for s in arr:
        # if cnt[s] > 1:
        #   continue
        if cnt[s] <= 1:
          if k == 1:
            return s
          k -= 1
      return ""
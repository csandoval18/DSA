from typing import List


class Solution:
  def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    n = len(arr)
    prefixXOR = [0] * n
    prefixXOR [0] = arr[0]
    
    for i in range(1, n):
      prefixXOR[i] = prefixXOR[i-1] ^ arr[i]
    
    res = []
    for left, right in queries:
      if left == 0:
        res.append(prefixXOR[right])
      else:
        res.append(prefixXOR[right] ^ prefixXOR[left - 1])
        
    return res

arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
s = Solution()
print(s.xorQueries(arr, queries))
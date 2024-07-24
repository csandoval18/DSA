from heapq import heappop, heappush
from typing import Counter, List


class Solution:
  def frequencySort(self, nums: List[int]) -> List[int]:
    hm = {}
    
    for num in nums:
      hm[num] = hm.get(num, 0)+1
    
    sorted_nums = sorted(nums, key=lambda x: (hm[x], -x))
    # hm.sort(key = lambda x: x[1]) # Alternate
    return sorted_nums
  
  # hm[1]: refers to the frequency of the element
  # -item[0]: refers to the negation of the element value
    
  # When you sort a list of tuples, Python sorts by the first element of the tuple first. 
  # If there's a tie, it then sorts by the second element, and so on.
  
  # In this specific case:
  # The list is sorted primarily by item[1], which is the frequency of each  
  
class Solution1:
  def frequencySort(self, nums: List[int]) -> List[int]:
    c = Counter(nums)
    hq = []
    for num in c:
      heappush(hq, (c[num], -i))
      
    res = []
    while(hq):
      x = heappop(hq)
      for i in range(x[0]):
        res.append(-x[1])
        
    return res
    
nums = [1,1,2,2,2,3] # Output: [3,1,1,2,2,2]
s = Solution()
print(s.frequencySort(nums))


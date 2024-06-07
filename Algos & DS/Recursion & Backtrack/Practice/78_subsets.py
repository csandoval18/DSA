from typing import List


class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res = []
    
    def bt(i: int, ds: List[int]):
      if i == n:
        res.append(ds[:])
        return
        
      ds.append(nums[i])
      bt(i+1, ds)
      ds.pop()
      bt(i+1, ds)
    
    bt(0, [])
    return res
  
s = Solution()
nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
print(s.subsets(nums))

# nums = [0]
# Output: [[],[0]]
# print(s.subsets(nums))
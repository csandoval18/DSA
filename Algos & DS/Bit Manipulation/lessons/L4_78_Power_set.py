from typing import List

# Using recursion refresher

class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    def helper(i: int, ds: List[int]) -> None:
      if i == len(nums):
        res.append(ds[:])
        return
      
      ds.append(nums[i])
      helper(i+1, ds)
      ds.pop()
      helper(i+1, ds)

    res = []
    helper(0, [])
    return res
    
    
  # New method using bit manipulation
  
  '''
          0 1 2
  nums = [1,2,3]

  2 1 0
  -----
  0 0 0 => []
  0 0 1 => [1]
  0 1 0 => [2]
  0 1 1 => [1,2]
  1 0 0 => [3]
  1 0 1 => [1, 3]
  1 1 0 => [2,3]
  1 1 1 => [1,2,3]

  '''
  # TC: O(N*2^N) | SC: O((2^N)*N)
  def subsetsBitManipulation(self, nums: List[int]) -> List[List[int]]:
    res = []
    subsets = 1 << len(nums) # 2^N = 2^3 = 8
    
    for N in range(subsets): # O(2^n)
      ds = []
      for i in range(len(nums)): # O(n)
        if N & (1 << i): # Check if i'th bit is set or not
          ds.append(nums[i])
      res.append(ds)
    return res


nums = [1,2,3]
s = Solution()
print(s.subsets(nums))
print(s.subsetsBitManipulation(nums))
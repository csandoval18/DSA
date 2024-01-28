from typing import List

def subsetsWithDupStrivers(nums: List[int]) -> List[List[int]]:
  res = []
  subsequence = []

  def findSubsets(idx: int):
    res.append(subsequence.copy())
    
    for i in range(idx, len(nums)):
      if i != idx and nums[i] == nums[i-1]:
        continue
      subsequence.append(nums[i])
      findSubsets(i+1)
      subsequence.pop()
      
  
  nums.sort()
  findSubsets(0)
  return res

def subsetsWithDup(nums: List[int])-> List[List[int]]:
  def findSubsets(idx: int, nums: List[int], subsequence: List[int], res: List[List[int]]) -> List[List[int]]:
    n = len(nums)
    res.append(subsequence.copy())
    
    for i in range(idx, n):
      if i != idx and nums[i] == nums[i-1]:
        continue
      subsequence.append(nums[i])
      findSubsets(i+1, nums, subsequence, res)
      subsequence.pop()
    
  res = []
  subsequence = []
  nums.sort()
  findSubsets(0, nums, subsequence, res)
  return res

nums = [1,2,3]
print(subsetsWithDupStrivers(nums))
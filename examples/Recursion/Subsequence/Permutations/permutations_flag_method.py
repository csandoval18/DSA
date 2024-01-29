from typing import List

def permute(nums: [int]) -> [[int]]:
  n = len(nums)
  res = []
  ds = []
  
  def util(nums: List[int], freq: List[int]):
    if len(ds) == n:
      res.append(ds[:])
      return
      
    for i in range(n):
      if freq[i] == False:
        ds.append(nums[i])
        freq[i] = 1
        util(nums, freq)
        freq[i] = 0
        ds.pop()
    
  freq = [0] * n
  util(nums, freq)
  return res
  
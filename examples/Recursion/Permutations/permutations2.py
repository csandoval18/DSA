from typing import List

# BF Backtracking
def permuteUniqueBF(nums: List[int]):
  n = len(nums)
  res = []
  freq = [0] * n
  
  def backtrack(ds: [int]):
    if len(ds) == n:
      ds.append(nums[:])
      return
      
    for i in range(n):
      if not freq[i]:
        ds.append(nums[i])
        freq[i] = 1
        backtrack(freq, ds)
        ds.pop()
        freq[i] = 0
    
    backtrack(freq)
    res.sort()
    return res
from typing import List

# BF Backtracking
def permuteUniqueBF(nums: List[int]):
  n = len(nums)
  res = []
  freq = [0] * n
  
  def backtrack(idx: int, ds: [int]):
    if idx == n-1:
      ds.append(nums[:])
      return
      
    for i in range(n):
      if not freq[i]:
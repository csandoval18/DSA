from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
  n = len(candidates)
  def backtrack(target: int, idx: int, ds: List[int]) -> None:
    if idx == n:
      if target == 0:
        res.append(ds[:])
      return
  
    # The idx is not increased to account for duplicates
    if candidates[idx] <= target:
      ds.append(candidates[idx])
      backtrack(target-candidates[idx], idx, ds)
      ds.pop()
    backtrack(target, idx+1, ds)
      
  
  res = []